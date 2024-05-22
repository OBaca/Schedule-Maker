from data.constants import *

class Worker:
    def __init__(self, position, min_shifts=4, max_shifts=6, max_nights=2,consecutive_nights='Y', eightx2=1):
        self.availability_position = position
        self.availability = [""]*7
        self.can_work = [True]*7
        self.min_shifts = min_shifts
        self.shifts_counter = 0
        self.max_shifts = max_shifts
        self.nights_counter = 0
        self.max_nights = max_nights
        self.consecutive_nights = convert_consecutive_nights_to_bool(consecutive_nights)
        self.eightx2_counter = 0 #8 hours of work, 8 hours of rest, 8 hours of work
        self.max_eightx2 = eightx2

    

    '''This function return worker position when try to print a worker.'''
    def  __str__(self):
        return self.availability_position



    ''' This function get from the excel file the worker availability to work on each day. '''
    def get_availability(self, ws):
        worker_row_position = self.availability_position[-1]
        #           B        C          D           E           F           G          H    
        #DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        # 66 - represent B in ascii
        for i in range(len(DAYS)):
            temp = chr(66 + i) + str(worker_row_position)
            if ws[temp].value == None:
                self.availability[i] = ""
            else:
                self.availability[i] = ws[temp].value
    


    ''' This function check the worker availability to work on each shift.'''
    def check_availability(self, day, day_num, shift_num):
        availability = self.availability[day_num]
        availability=availability.split(".")
        morning = []
        noon = []
        night = []
        if day.amount_of_shifts==4:
            morning = [0]
            noon=[1]
            night = [2,3]
        if day.amount_of_shifts ==5:
            morning = [0]
            noon=[1,3]
            night = [2,5]
        if day.amount_of_shifts ==6:
            morning=[0,3]
            noon=[1,4]
            night=[2,5]

        for i in range(len(availability)):
            if availability[0] =='':
                return False
            if (availability[i][0] in 'af' or availability[i] == 'morning') and shift_num in morning:
                return True
            if (availability[i][0] in 'bf' or availability[i] == 'noon') and shift_num in noon:
                return True
            if (availability[i][0] in 'cf' or availability[i] == 'night') and shift_num in night:
                return True
        return False



    ''' This function prints the availability of the worker. '''
    def print_availability(self):
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        print("===============")
        for i in range(7):
            print(days[i] + ": " + str(self.availability[i]))
        print("===============")



''' This function create the workers and assign them to the workers array'''
def create_workers(ws):
    workers = []
    wb_settings = load_workbook("Template/settings.xlsx")
    ws_settings = wb_settings.active
    amount_of_workers = ws_settings[SETTINGS_AMOUNT_OF_WORKERS].value
    wb_settings.close()

    for i in range(2,2+amount_of_workers):
        workers.append(Worker(f"{WORKER_POSITION}{i}",max_shifts= ws[f"{AMOUNT_OF_SHIFTS_POS}{i}"].value,max_nights= ws[f"{AMOUNT_OF_NIGHT_POS}{i}"].value,consecutive_nights=ws[f"{CONSECUTIVE_NIGHTS_POS}{i}"].value, eightx2=ws[f"{EIGHTX2_AMOUNT_POS}{i}"].value))
    for worker in workers:
        worker.get_availability(ws)

    return workers



''' This function prints the worker stats, used for debug.'''
def print_workers_stats(workers):
    for worker in workers:
        print('-~-~-~-~-~-')
        print('name:' + worker.availability_position)
        print('min shift: ' + str(worker.min_shifts))
        print('max shifts: ' + str(worker.max_shifts))
        print('shifts counter: '+ str(worker.shifts_counter))
        print('nights counter: ' + str(worker.nights_counter))
        print('amount of eightx2: ' + str(worker.eightx2))



'''This function returns True/False depends on the worker constraint that filled by the manager.'''
def convert_consecutive_nights_to_bool(consecutive_nights):
    if consecutive_nights == 'Y':
        return True
    else:
        return False
