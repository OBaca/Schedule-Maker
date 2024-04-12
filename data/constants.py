import random
from openpyxl import Workbook, load_workbook
from openpyxl.styles import PatternFill
import time
import os
from datetime import datetime

DAYS =  ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
BACKUP_WORKER = 'A9'
START_OF_REQUEST_TABLE = 'L'
START_OF_SCHEDULE = 'A'
NIGHTS_LIMIT = 2
AMOUNT_OF_WORKERS = 'M8'
AMOUNT_OF_SHIFTS_POS = 'I'
WORKER_POSITION = 'A'
AMOUNT_OF_WORKERS_POS = 'M20'
AMOUNT_OF_NIGHT_POS = 'K'
CONSECUTIVE_NIGHTS_POS = 'M'
SHIFT_COUNTER_POS_FINAL_RESULT = 'U'
COMMENT_POS_ON_CONSTRAINTS = 'O'
EIGHTX2_AMOUNT_POS = 'Q'

'''This function creates a folder for every new week and creates a schedule.'''
def save_folder_by_week():
    current_date = datetime.now()
    week_folder_name = f"Week_{current_date.isocalendar()[1]}_Year_{current_date.year}"
    week_folder_path = os.path.join("RESULTS/",week_folder_name)
    if not os.path.exists(week_folder_path):
        os.makedirs(week_folder_path)
    
    i=0
    while os.path.exists(f"{week_folder_path}/({i}) סידור מוכן.xlsx"):
        i+=1
    return f"{week_folder_path}/({i}) סידור מוכן.xlsx"
