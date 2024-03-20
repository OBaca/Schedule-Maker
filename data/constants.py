import random
from openpyxl import Workbook, load_workbook
from openpyxl.styles import PatternFill
import time

DAYS =  ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
BACKUP_WORKER = 'A9'
START_OF_REQUEST_TABLE = 'L'
START_OF_SCHEDULE = 'A'
NIGHTS_LIMIT = 2