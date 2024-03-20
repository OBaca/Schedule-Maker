import random
from openpyxl import Workbook, load_workbook
from openpyxl.styles import PatternFill
import time

DAYS =  ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
BACKUP_WORKER = 'A9'
NIGHTS_LIMIT = 2