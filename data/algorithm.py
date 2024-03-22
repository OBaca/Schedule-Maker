import random
from data.day import *
from data.worker import *
from data.constants import *
from copy import deepcopy



def algorithm(manual=True):
    if manual:
        path = "manual/תבנית סידור.xlsx"
        wb = load_workbook(f"{path}")
        ws = wb.active
        
        wb2 = load_workbook("manual/תבנית זמינות.xlsx")
        ws2 = wb2.active

        
        
    else:
        path = "automate/תבנית סידור.xlsx"
        wb = load_workbook(f"{path}")
        ws = wb.active
        
        wb2 = load_workbook("automate/תבנית זמינות.xlsx")
        ws2 = wb2.active

        
        

    


    #days = {'Sunday':'B', 'Monday':'C', 'Tuesday':'D', 'Wednesday':'E', 'Thursday':'F', 'Friday':'G', 'Saturday':'H'}
    # Need to create a function to read from a file that knows how many shifts every day
    amount_of_shifts = [4,4,4,4,4,5,6]
    schedule = create_schedule(amount_of_shifts)
    workers = create_workers(ws2)
    
    #transfer_workers_names(ws,ws2,len(workers))
    for i in range(2,len(workers)+3):
        ws['J' + str(i)] = ws2['A'+str(i)].value
    wb.save(f"{path}")
    
    
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
    
    
    print(len(workers[0].availability[0]))

    transfer_constraints_to_schedule(wb,ws,ws2,len(workers),path)

    make_excel_schedule(schedule,path)
