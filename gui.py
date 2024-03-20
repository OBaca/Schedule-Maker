from customtkinter import *
import tkinter

set_appearance_mode("dark")
set_default_color_theme("green")

app = CTk()
app.geometry("650x500")



frame = CTkFrame(master=app)
frame.pack(pady=20,padx=30, fill="both", expand=True)

label = CTkLabel(master=frame,text="Make a schedule")
label.pack(pady=12,padx=10)

name = tkinter.StringVar()
entry1 = CTkEntry(master=frame, placeholder_text="הסידור שם", textvariable=name)
entry1.pack(pady=12,padx=10)


amount_of_workers = tkinter.StringVar()
entry2 = CTkEntry(master=frame, placeholder_text="עובדים כמות",textvariable=amount_of_workers)
entry2.pack(pady=12,padx=10)


def add_worker(amount,tabview):
    workers = []
    for i in range(int(amount)):
        worker = tkinter.StringVar()
        workers.append(CTkEntry(master=tabview.tab(f"Worker {i}"), placeholder_text="worker name", textvariable=worker))
        workers[i].pack(pady=12,padx=10)

    for i in range(len(workers)):
        print(workers[i].get())

    

def manually_fill():
    
    amount = entry2.get()
    name = entry1.get()
    print(name)
    print(amount)
    tabview = CTkTabview(master=frame)
    tabview.pack(padx=20,pady=20)
    for i in range(int(amount)):
        tabview.add(f"Worker {i}")
    
    add_worker(amount,tabview)
    '''
    worker1 = tkinter.StringVar()
    worker1 = CTkEntry(master=tabview.tab("Worker 1"), placeholder_text="worker name", textvariable=worker1)
    worker1.pack(pady=12,padx=10)'''
    
    '''def checkbox_event():
        print("checkbox toggled, current value:", check_var.get())

    check_var = StringVar(value="on")
    checkbox = CTkCheckBox(app, text="CTkCheckBox", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
    checkbox.pack(pady=12,padx=10)
'''
    button2 = CTkButton(master=frame, text="Submit", command=submit)
    button2.pack(pady=12,padx=10)


def submit():
    print("submit")

button = CTkButton(master=frame, text="manually fill", command=manually_fill)
button.pack(pady=12,padx=10)








'''#for i in range(entry2):
tabview.add(f"Tab 1")
tabview.add(f"Tab 2")

label_1 = CTkLabel(master=tabview.tab("Tab 1"), text="This is Tab 1")
label_1.pack(padx=20, pady=20)

label_2 = CTkLabel(master=tabview.tab("Tab 2"), text="This is Tab 2")
label_2.pack(padx=20, pady=20)'''

app.mainloop()


