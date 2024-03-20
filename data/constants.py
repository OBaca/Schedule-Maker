import random
from openpyxl import Workbook, load_workbook
import time

DAYS =  ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
BACKUP_WORKER = 'A9'
NIGHTS_LIMIT = 2