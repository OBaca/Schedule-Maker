from data.constants import *

class Day:
    def __init__(self, id, name, amount_of_shifts=4):
        self.id = id
        self.name = name
        self.amount_of_shifts = amount_of_shifts
        self.shifts = [BACKUP_WORKER for i in range(self.amount_of_shifts) ]


    def __str__(self):
        return self.name
    


    '''
    regular days - 0 - morning, 1-noon, 2,3-night
    friday - 0 morning, 1,3 - noon, 2,4 - night
    Saturday - 0,3 - morning, 1,4 - noon, 2,5 - night
    worker can't work on the morning when yesterday he worked at night
    '''
    def shift_ground_rules(self, worker,position, yesterday):
        if yesterday==None:
            return True
        # if today is sunday, then need to check the last shifts arrangement #

        if self.amount_of_shifts in [4,5]:
            if position == 0 and (worker.availability_position in yesterday.shifts[2] or worker.availability_position in yesterday.shifts[3]):
                return False
        elif self.amount_of_shifts==6:
            if position in [0,3] and (worker.availability_position in yesterday.shifts[2] or worker.availability_position in yesterday.shifts[4]):
                return False
        
        return True
        


''' This function create schedule. '''
def create_schedule(amount_of_shifts):
    schedule = []

    for i in range(len(DAYS)):
        if amount_of_shifts[i] == None:
            print("You didn't put any numbers in the required cells")
        schedule.append(Day(i,DAYS[i],amount_of_shifts[i]))


    return schedule


    

''' This function creates an excel schedule from the availability excel sheet.'''
def make_excel_schedule(schedule,path):
    wb = load_workbook(f"{path}/תבנית סידור.xlsx")
    ws = wb.active

    day_counter=0
    for day in schedule:
        for i in range(len(day.shifts)):
            # placing the right names at the right shifts
            ws[chr(66 + day_counter) + str(get_line_from_template(day.amount_of_shifts, i)) ] = ws['J' + day.shifts[i][1]].value
            if day.shifts[i] == BACKUP_WORKER:
                ws[chr(66 + day_counter) + str(get_line_from_template(day.amount_of_shifts, i))].fill = PatternFill(start_color='FFFF0000',end_color='FFFF0000',fill_type='solid')
        day_counter+=1

    wb.save(f"{save_folder_by_week()}")


def get_line_from_template(amount_of_shifts, shift_i):
    match shift_i:
        case 0:
            return 4
        case 1:
            return 5
        case 2:
            return 6
        case 3:
            if amount_of_shifts==4:
                return 10
            elif amount_of_shifts==5:
                return 9
            elif amount_of_shifts==6:
                return 8
        case 4:
            if amount_of_shifts==5:
                return 10
            elif amount_of_shifts==6:
                return 9
        case 5:
            return 10

        case _:
            print("Trying to put name of a worker in an unknown cell")
            return 0 
    

''' This function print the schedule.'''
def print_schedule(schedule):
    for day in schedule:
        print(str(day)+": " )
        print(day.shifts)


''' This function generate shifts to the workers randomly.'''
def assign_workers(workers, schedule):
    
    counter = 0
    backup_worker = False
    ''' Need to add yesterday to the function so we can get the last week saturday night position'''
    yesterday = None
    
    for day in schedule:
        
        for shift in range(day.amount_of_shifts):
            exclude_worker = []
            # get a random worker
            curr_worker=random.randint(0,len(workers)-1)

            while not workers[curr_worker].can_work[counter] or not workers[curr_worker].check_availability(day, counter, shift) \
                    or not day.shift_ground_rules(workers[curr_worker],shift,yesterday) or workers[curr_worker].shifts_counter >= workers[curr_worker].max_shifts\
                        or workers[curr_worker].nights_counter >=workers[curr_worker].max_nights \
                            or (workers[curr_worker].consecutive_nights == False and check_consecutive_nights(workers[curr_worker],yesterday)) \
                                or (workers[curr_worker].eightx2_counter >= workers[curr_worker].max_eightx2 and check_for_eightX2(schedule, counter, shift, workers[curr_worker])):
                
                exclude_worker.append(curr_worker)
                if len(exclude_worker)==len(workers):
                    backup_worker = True
                    break
                curr_worker=random.choice(list(set([x for x in range(len(workers))]) - set(exclude_worker)))

            if backup_worker:
                # DONT CHANGE ANYTHING - because the default is backup worker
                backup_worker=False
                continue

            # updating settings
            day.shifts[shift]=workers[curr_worker].availability_position
            workers[curr_worker].can_work[counter] = False
            workers[curr_worker].shifts_counter +=1
            if check_if_night_shift(shift,day.amount_of_shifts):
                workers[curr_worker].nights_counter +=1
            
            #check for eightx2 shifts
            if check_for_eightX2(schedule, counter, shift, workers[curr_worker]):
                workers[curr_worker].eightx2_counter +=1
                
            #time.sleep(0.001)  #used to make a delay for the random seed
        
        yesterday = day
        counter+=1
        
    
    
def count_backup_workers(schedule):
    count=0
    for day in schedule:
        for i in range(len(day.shifts)):
            if day.shifts[i] == BACKUP_WORKER:
                count+=1
    
    return count


'''This function check if the worker would do 8-8 shift.'''
def check_for_eightX2(schedule, day_num, shift_num, curr_worker):
    # the worker would never do saturday noon/night and sunday morning/noon
    if day_num == -1:
            return True

    if schedule[day_num].amount_of_shifts == 4:
        # if the worker works today at noon and yesterday he worked at night
        if shift_num == 1 and (schedule[day_num-1].shifts[2] == curr_worker.availability_position or schedule[day_num-1].shifts[3] == curr_worker.availability_position):
            return True
        # if the worker works today at the morning and yesterday he worked at noon
        if shift_num == 0 and schedule[day_num-1].shifts[1] == curr_worker.availability_position:
            return True
        # and the option to work on the same day twice doesn't apply.

    elif schedule[day_num].amount_of_shifts == 5:
        # if the worker works today at noon and yesterday he worked at night
        if (shift_num == 1 or shift_num==3) and (schedule[day_num-1].shifts[2] == curr_worker.availability_position or schedule[day_num-1].shifts[3] == curr_worker.availability_position):
            return True
        # if the worker works today at the morning and yesterday he worked at noon
        if shift_num == 0 and schedule[day_num-1].shifts[1] == curr_worker.availability_position:
            return True
    
    elif schedule[day_num].amount_of_shifts == 6:
        # if the worker works today at noon and yesterday he worked at night
        if (shift_num == 1 or shift_num==4) and (schedule[day_num-1].shifts[2] == curr_worker.availability_position or schedule[day_num-1].shifts[4] == curr_worker.availability_position):
            return True
        # if the worker works today at the morning and yesterday he worked at noon
        if (shift_num == 0 or shift_num==3) and (schedule[day_num-1].shifts[1] == curr_worker.availability_position or schedule[day_num-1].shifts[3] == curr_worker.availability_position):
            return True
    
    else:
        return False
    


'''This function loops over the schedule and check where the backup workers are if they can be replaced'''
def revisit_backup_spots(schedule, workers):
    yesterday = None
    counter=0
    for day in schedule:
        for shift in range(len(day.shifts)):
            if day.shifts[shift] == BACKUP_WORKER:
                for worker in workers:
                    if (worker.can_work[day.id] and worker.check_availability(day, day.id, shift) \
                        and day.shift_ground_rules(worker,shift,yesterday) \
                             and worker.shifts_counter < worker.max_shifts):
                        if not check_if_night_shift(shift,day.amount_of_shifts) or \
                            (worker.nights_counter <worker.max_nights and  check_if_night_shift(shift,day.amount_of_shifts)):
                            
                            day.shifts[shift] = worker.availability_position
                            worker.shifts_counter +=1
                            worker.can_work[day.id] = False
                            if check_if_night_shift(shift,day.amount_of_shifts):
                                worker.nights_counter +=1
                    
        yesterday = day
        counter+=1
    

''' This function add the constraints table to the schedule for easy access.'''
def transfer_constraints_to_schedule(wb,ws,ws2, amount_of_workers,path, workers):

    for i in range(1,amount_of_workers+2):
        for j in range(10):
            ws[chr(ord(START_OF_REQUEST_TABLE)+j) + str(i)] = ws2[chr(ord(START_OF_SCHEDULE)+j) +str(i)].value

        # Adding the comment section for each worker to the table.
        ws['L'+ str(i)] = ws2[COMMENT_POS_ON_CONSTRAINTS+str(i)].value
        # adding yellow color if there is a comment on a worker and resetting the cell
        ws['L'+ str(i)].fill = PatternFill(fill_type=None)
        if ws['L'+ str(i)].value != None:
            color = '00FFFF00' #yellow color
            ws['L'+ str(i)].fill = PatternFill(start_color=color, end_color=color, fill_type='solid')
        


    ws[chr(ord(SHIFT_COUNTER_POS_FINAL_RESULT)) + '1'] = 'AMOUNT:'
    for curr_workers in range(amount_of_workers):
        ws[chr(ord(SHIFT_COUNTER_POS_FINAL_RESULT)) + str(curr_workers+2)] = workers[curr_workers].shifts_counter    

    wb.save(f"{path}/תבנית סידור.xlsx")


'''This function returns True if a shift is a night shift'''
def check_if_night_shift(shift_num,amount_of_shifts):
    if amount_of_shifts == 4 and shift_num in [2,3] or \
                            amount_of_shifts == 5 and shift_num in [2,4] or \
                                amount_of_shifts == 6 and shift_num in [2,5]:
        return True
    return False


'''This function check if the worker would work two consecutive nights.'''
def check_consecutive_nights(worker,yesterday):
    if not yesterday:
        return False
    if yesterday.amount_of_shifts == 4:
        if yesterday.shifts[2] == worker.availability_position or yesterday.shifts[3] == worker.availability_position:
            return True
    elif yesterday.amount_of_shifts == 5:
        if yesterday.shifts[2] == worker.availability_position or yesterday.shifts[4] == worker.availability_position:
            return True
    elif yesterday.amount_of_shifts == 6:
        if yesterday.shifts[2] == worker.availability_position or yesterday.shifts[5] == worker.availability_position:
            return True
    else:
        return False
