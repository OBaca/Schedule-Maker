from data.constants import *
from copy import copy

def create_new_table(name,amount_workers,amount_stations):
    '''
    wb_set_table = load_workbook("create_new_table/new_table.xlsx")
    ws_set_table = wb_set_table.active
    '''
    

    wb_template = load_workbook(f"Template/תבנית_סידור_עמדה_{amount_stations}.xlsx")
    ws_template = wb_template.active

    wb_constraints = load_workbook("Template/תבנית_זמינות_עמדה.xlsx")
    ws_constraints = wb_constraints.active

    #settings
    STATION1_TABLE_NAME = 'A1'
    
    try:
        ws_template[STATION1_TABLE_NAME] = name
    except:
        print("You need to write the name in english")

    
    wb_template.save("Template/תבנית סידור.xlsx")

    colors = ['00FF00FF','0000FFFF','0000FF00','00008080','00FF8080','00808000']
    colors_line_to_avoid = [2,3,4,5,6,7,8,10,12,14,15,16,18]
    color_idx = 0
    ws_constraints.insert_rows(3, amount=amount_workers -1)
    for i in range(3,amount_workers+2 ):
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

    wb_constraints.save("Template/תבנית זמינות.xlsx")
    wb_constraints.close()
    wb_template.close()