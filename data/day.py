from data.constants import *
import os

class Day:
    def __init__(self, id, name, amount_of_shifts=4):
        self.id = id
        self.name = name
        self.amount_of_shifts = amount_of_shifts
        self.shifts = ["A9" for i in range(self.amount_of_shifts) ]


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
def make_excel_schedule(ws2,schedule):
    wb = load_workbook("Template/תבנית סידור.xlsx")
    ws = wb.active
    ''' Position 0: front stage, Position 1: back stage'''
    morning_line = [4,8]
    noon_line = [5,9]
    night_line = [6,10]

    day_counter=0
    for day in schedule:
        for i in range(len(day.shifts)):
            # placing the right names at the right shifts
            ws[chr(66 + day_counter) + str(get_line_from_template(day.amount_of_shifts, i)) ] = ws['J' + day.shifts[i][1]].value
            if day.shifts[i] == 'A9':
                ws[chr(66 + day_counter) + str(get_line_from_template(day.amount_of_shifts, i))].fill = PatternFill(start_color='FFFF0000',end_color='FFFF0000',fill_type='solid')
        day_counter+=1

    i=0
    while os.path.exists(f"({i}) סידור מוכן.xlsx"):
        i+=1
    
    wb.save(f"({i}) סידור מוכן.xlsx")


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
                        or workers[curr_worker].nights_counter >=NIGHTS_LIMIT:
                
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
            if day.amount_of_shifts == 4 and shift in [2,3] or \
               day.amount_of_shifts == 5 and shift in [2,4] or \
               day.amount_of_shifts == 6 and shift in [2,5]:
                workers[curr_worker].nights_counter +=1
            
            # schedule, day_num, shift_num, curr_worker
            if check_for_eightX2(schedule,day.id, shift, curr_worker):
                pass
                
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


def check_for_eightX2(schedule, day_num, shift_num, curr_worker):
    if schedule[day_num].amount_of_shifts == 4:
        # if the worker works today at noon and yesterday he worked at night
        if shift_num == 1 and (schedule[day_num-1].shifts[2] == curr_worker or schedule[day_num-1].shifts[3] == curr_worker):
            return True
        # if the worker works today at the morning and yesterday he worked at noon
        if shift_num == 0 and schedule[day_num-1].shifts[1] == curr_worker:
            return True
        # and the option to work on the same day twice doesn't apply.

    elif schedule[day_num].amount_of_shifts == 5:
        # if the worker works today at noon and yesterday he worked at night
        if (shift_num == 1 or shift_num==3) and (schedule[day_num-1].shifts[2] == curr_worker or schedule[day_num-1].shifts[3] == curr_worker):
            return True
        # if the worker works today at the morning and yesterday he worked at noon
        if shift_num == 0 and schedule[day_num-1].shifts[1] == curr_worker:
            return True
    
    elif schedule[day_num].amount_of_shifts == 6:
        # if the worker works today at noon and yesterday he worked at night
        if (shift_num == 1 or shift_num==4) and (schedule[day_num-1].shifts[2] == curr_worker or schedule[day_num-1].shifts[4] == curr_worker):
            return True
        # if the worker works today at the morning and yesterday he worked at noon
        if (shift_num == 0 or shift_num==3) and (schedule[day_num-1].shifts[1] == curr_worker or schedule[day_num-1].shifts[3] == curr_worker):
            return True
    
    else:
        return False
    

# delete maybe?
def backtracking(schedule, current_day, workers, min_backup_workers, min_backup_schedule):
    if current_day == len(schedule):
        # Base case: All days are assigned, return the schedule
        backup_workers_count = count_backup_workers(schedule)
        if backup_workers_count < min_backup_workers[0]:
            min_backup_workers[0] = backup_workers_count
            min_backup_schedule[0] = schedule
        return
    
    for worker in workers:
        for day in schedule:
            for shift in day.shifts:
                pass



def revisit_backup_spots(schedule, workers):
    yesterday = None
    for day in schedule:
        for shift in range(len(day.shifts)):
            if day.shifts[shift] == BACKUP_WORKER:
                
                for worker in workers:
                    if worker.can_work[day.id] and worker.check_availability(day, day.id, shift) \
                        and day.shift_ground_rules(worker,shift,yesterday) \
                            and worker.shifts_counter < worker.max_shifts \
                                and worker.nights_counter <NIGHTS_LIMIT:
                        day.shifts[shift] = worker.availability_position
                        worker.shifts_counter +=1
                        worker.can_work[day.id] = False
                        print('yea make a change')
                        if day.amount_of_shifts == 4 and shift in [2,3] or \
                            day.amount_of_shifts == 5 and shift in [2,4] or \
                                day.amount_of_shifts == 6 and shift in [2,5]:
                            worker.nights_counter +=1
                    
        yesterday = day
    

''' This function add the limitation table to the schedule for easy access.'''
def transfer_limitation_to_schedule(wb,ws,ws2, amount_of_workers):

    for i in range(1,amount_of_workers+2):
        for j in range(10):
            ws[chr(ord('L')+j) + str(i)] = ws2[chr(ord('A')+j) +str(i)].value
    
    wb.save("Template/תבנית סידור.xlsx")
