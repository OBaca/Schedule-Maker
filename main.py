import random
from data.day import *
from data.worker import *
from data.constants import *
from copy import deepcopy

AMOUNT_OF_WORKERS = 'M8'
AMOUNT_OF_SHIFTS = 'I'
WORKER_POSITION = 'A'


def main(manual=True):
    if manual:
        wb = load_workbook("Template/תבנית סידור.xlsx")
        ws = wb.active
        
        wb2 = load_workbook("Template/תבנית זמינות.xlsx")
        ws2 = wb2.active
    else:
        wb = load_workbook("automate/תבנית סידור.xlsx")
        ws = wb.active
        
        wb2 = load_workbook("automate/זמינות.xlsx")
        ws2 = wb2.active

    


    #days = {'Sunday':'B', 'Monday':'C', 'Tuesday':'D', 'Wednesday':'E', 'Thursday':'F', 'Friday':'G', 'Saturday':'H'}
    # Need to create a function to read from a file that knows how many shifts every day
    amount_of_shifts = [4,4,4,4,4,5,6]
    schedule = create_schedule(amount_of_shifts)
    workers = create_workers(ws2)
    
    #transfer_workers_names(ws,ws2,len(workers))
    for i in range(2,len(workers)+3):
        ws['J' + str(i)] = ws2['A'+str(i)].value
    wb.save("Template/תבנית סידור.xlsx")
    
    '''
    for day in schedule:
        print(day)

    for worker in workers:
        print(worker)
        #worker.print_availability()
    
    for worker in workers:
        print(worker.availability)
    ''' 
    print("=-=-=-=-=-=-=-=-=")
    
    best_schedule = []
    best_workers = []
    min_backup_workers=10
    
    for i in range(2500):
        schedule_temp = deepcopy(schedule)
        workers_temp = deepcopy(workers)
        random.seed()

        assign_workers(workers_temp,schedule_temp)
        curr_backup_counter = count_backup_workers(schedule_temp)
        
        if curr_backup_counter < min_backup_workers:
            
            min_backup_workers = curr_backup_counter
            best_schedule = deepcopy(schedule_temp)
            best_workers = deepcopy(workers_temp)
        
    schedule = best_schedule
    workers = best_workers
    '''
    # revisit all the backup spots and check if we can still place regular worker on the spot and it will not affect him.
    for i in range(10):
        schedule_temp = deepcopy(schedule)
        workers_temp = deepcopy(workers)
        revisit_backup_spots(schedule_temp,workers_temp)
        curr_backup_counter = count_backup_workers(schedule_temp)
        
        if curr_backup_counter < min_backup_workers: 
            min_backup_workers = curr_backup_counter
            best_schedule = deepcopy(schedule_temp)
            best_workers = deepcopy(workers_temp)

    schedule = best_schedule
    workers = best_workers
    '''
    print_schedule(schedule)
    print(min_backup_workers)
    print_workers_stats(workers)
    # testing
    '''word = "a.b[12:22]"
    print(word.split('.'))

    woo = "A2"
    print(woo[-1])'''
    
    make_excel_schedule(ws2,schedule)





if __name__ == "__main__":
    main()
    