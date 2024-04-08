# Schedule-Maker

```
I once saw my manager working on the schedule for next week,
and he told me that it took him almost 4 hours just to gather every worker's constraints
and ensure that each worker received a well-balanced set of shifts.
So, I suggested to him, 'Why wouldn't I make a program for it?'
Now, my manager can create a schedule in just 10 minutes, with 5 of those minutes spent waiting for the water to boil for coffee.
```

![Project Image](https://i.postimg.cc/wTVkZY1M/empty-sched.png)

FINAL RESULT

![Example-Picture](https://i.postimg.cc/yNy7dTyF/example-sched.png)


> 

---

### Table of Contents

- [Description](#description)
- [Setup](#Setup)
- [Create-a-Table](#Create-a-Table)
- [How-To-Use](#How-To-use)


---

## Description

 Crafting dynamic schedules and implementing automated worker
 assignments, empowering your team to maximize productivity while
 easing the burden on management.
 * Create a Google Form so workers can input their constraints for the next week.
 * The manager clicks on a single button, and voilà, a working schedule for the next week is generated.

   
 In this schedule, we take into consideration:

 * The manager can choose the maximum number of shifts a worker can work in a week.
 * The Google Form adjusts the workers' constraints so that it doesn't assign a specific worker to a shift they can't work.
 * The worker can also add comments if they have special requests, which will be highlighted for the manager.
 * The manager can choose the maximum amount of night shifts for each worker.
 * The manager can decide if a worker can work two nights in a row or not.
 * The manager can choose the number of 8-8 shifts (8 hours of work, 8 hours of rest, 8 hours of work).
 * If none of the workers can work a certain shift, a backup worker will be assigned. The manager can choose to replace it with a regular worker or call for backup.
 * The manager can determine the number of shifts each day and the number of stands.
 * The manager can modify the labels of the constraints for their convenience.
 * The end result will display the schedule for the next week alongside the workers' constraints.
 

[Back To The Top](#Schedule-Maker)

---

## Setup
  ##### ***Step 1:*** Google form setup
  1. copy this [link](https://docs.google.com/forms/d/1m170bzx7qc6tQB1d72rywQjbOEVdoDulN0Wu6iPKG7M/copy): and save the form
  2. create google sheet:
     
![sheet](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXF2cWh1NW41dHlvOHFiOWRqd2xhM2tqdzlxamQ0cmp4ZmljcXVwNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xFqWJGhbwvl3ESqPqw/giphy.gif)

  4. After the Google Sheet and the Google Form are linked, you can send the link to your workers for them to fill out their constraints.

  ![sheet2](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExamNpZ3BtenU5azdrYmFhZmx6OTNxaW5lamV0YjZlZWJjYmsxNmEzMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IArR6NbTjfyOGJLVxJ/giphy.gif)
  ##### ***Step 2:*** Setup:
  ###### Windows Setup:
   - open cmd in the folder and write:
     ```pip install -r requirements.txt```
   - click on Schedule-Maker.exe
   - 
  ###### Mac Setup: 
   - Need to install python, openpyxl, customtkinter
   - Open terminal in the main folder and write: ```python main.py```
   - At this moment need to install the libraries manually, soon will be added .app file



 ##### ***Step 3:*** Link Google Sheets to Excel in Real Time
  1. Enter folder sheets and open the Excel file: "sheet".
  2. Follow this [Youtube video](https://www.youtube.com/watch?v=u__HU9fzsAY&ab_channel=ChesterTugwell) to link google sheets to the local excel file.
  3. Important: make sure you select in the properties "Refresh data when opening the file".


[Back To The Top](#Schedule-Maker)

---

## Create a Table

IN PROGRESS


[Back To The Top](#Schedule-Maker)

---

## How To Use
Firstly, workers send their constraints using the link provided in step 1 of the setup. Once everyone has sent their constraints:
1. Navigate to the folder 'sheets' and open 'sheet.xlsx'. Wait for it to update (approximately 5-10 seconds), then save and close it.
2. Click on Schedule-Maker.exe.
 ![exe-pic](https://i.postimg.cc/x84zZQkT/exe.png)

3. Now, you can click on the 'Automate' button, and it will generate a schedule for you, assigning all the workers based on their constraints.
4. Alternatively, you can manually change their constraints by clicking on the 'Manual' button:
![Manual-Schedule](https://i.postimg.cc/1tNhFcpC/manual-sched.png)

You can adjust the settings for your schedule as desired, then save it, and click 'Automate' again.
The final schedule will be located in the 'RESULTS' folder, with each week having its own folder. You can create as many schedules as you want and choose the one you prefer.


[Back To The Top](#Schedule-Maker)
