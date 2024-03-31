from data.constants import *
from copy import copy

def create_new_table():
    wb_set_table = load_workbook("create_new_table/new_table.xlsx")
    ws_set_table = wb_set_table.active

    wb_template = load_workbook("Template/תבנית עמדה1.xlsx")
    ws_template = wb_template.active

    wb_constraints = load_workbook("Template/תבנית זמינות1.xlsx")
    ws_constraints = wb_constraints.active

    #settings
    STATION1_TABLE_NAME = 'A1'
    NEW_TABLE_NAME = 'B2'
    BLACK_PATTERN = PatternFill(start_color='00000000',end_color='00000000',fill_type='solid')
    AMOUNT_OF_WORKERS_SETTINGS = 'B3'
    
    ws_template[STATION1_TABLE_NAME] = ws_set_table[NEW_TABLE_NAME].value

    
    wb_template.save("Template/copy_to_תבנית_סידור.xlsx")

    colors = ['00FF00FF','0000FFFF','0000FF00','00008080','00FF8080','00808000']
    colors_line_to_avoid = [2,3,4,5,6,7,8,10,12,14,15,16,18]
    color_idx = 0
    if isinstance(ws_set_table[AMOUNT_OF_WORKERS_SETTINGS].value,int):
        ws_constraints.insert_rows(3, amount=ws_set_table[AMOUNT_OF_WORKERS_SETTINGS].value -1)
        for i in range(3,ws_set_table[AMOUNT_OF_WORKERS_SETTINGS].value+2 ):
            if color_idx>=len(colors): color_idx=0    
            for c in range(1,19):
                ws_constraints.cell(i,c).font = copy(ws_constraints.cell(2,c).font)
                ws_constraints.cell(i,c).alignment = copy(ws_constraints.cell(2,c).alignment)
                ws_constraints.cell(i,c).border = copy(ws_constraints.cell(2,c).border)
                if c not in colors_line_to_avoid:
                    ws_constraints.cell(i,c).fill = PatternFill(start_color= colors[color_idx],end_color=colors[color_idx],fill_type='solid')
                else:
                    ws_constraints.cell(i,c).fill = copy(ws_constraints.cell(2,c).fill)
                ws_constraints.cell(i,c).value = ws_constraints.cell(i-1,c).value
            
            color_idx+=1

    wb_constraints.save("asdasd.xlsx")
    wb_set_table.close()