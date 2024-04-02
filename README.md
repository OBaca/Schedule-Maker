# Schedule-Maker

![Project Image](https://i.postimg.cc/wTVkZY1M/empty-sched.png)

> 

---

### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [In Progress](#Main-Menu-and-Costumes)
- [In Progress](#Gameplay)


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

## How To Use
  ##### ***Step 1:*** Google form setup
  1. copy this link: and save the form
  2. create google sheet:
     
![sheet](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXF2cWh1NW41dHlvOHFiOWRqd2xhM2tqdzlxamQ0cmp4ZmljcXVwNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xFqWJGhbwvl3ESqPqw/giphy.gif)

  4. After the Google Sheet and the Google Form are linked, you can send the link to your workers for them to fill out their constraints.

  ![sheet2](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExamNpZ3BtenU5azdrYmFhZmx6OTNxaW5lamV0YjZlZWJjYmsxNmEzMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IArR6NbTjfyOGJLVxJ/giphy.gif)
  ##### ***Step 2:*** Setup:
  ###### Windows Setup:
   - open cmd in the folder and write:
     ```pip install -r requirements.txt```
   - click on Schedule-Maker.exe
  ###### Mac Setup:
   - Open terminal in the folder and write:
     ```python setup.py py2app```
   - Click on Schedule-Maker.app



 ##### ***Step 3:*** Link Google Sheets to Excel in Real Time
  1. Enter folder sheets and open the Excel file: "sheet"
  2. Follow this gif steps below:


[Back To The Top](#Schedule-Maker)

---

## In Progress


[Back To The Top](#Schedule-Maker)

---

## In Progress


[Back To The Top](#Schedule-Maker)
