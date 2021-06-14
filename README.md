Project Name
Working hours tracker.

The user will enter his working hours and the data will be stored. The data will then be check against the official working hours and over/undertime will be calculated. The user will get an overview how many hours he worked per day and get a report how much over or undertime he currently has.
The programm will also include a possibility to see when the user usually generates over- or undertime. Using plotly visualization

Needed functions:
1. User working hour entries  - DONE
   1.1 Daily overview (current date)   - DONE
2. Official working hours store  - DONE stored in JSON
3. User working and official hours check  - DONE
    3.1. Print over or undertime  DONE
5. Print on which days most over- undertime is generated  - Reduced to specific day - DONE
6. Visualize data - DONE - Visualizing in Chart format and Plot for overtime - DONE

Step by step idea Frontend:

Mainpage:
1. User opens webapp
2. User sees functions to choose   
   2.1 Zeiterfassung   
   2.2 Übersicht   
   2.3 Analyse   
3. User chooses desired function   

Zeiterfassung:   
1. User sees fields with Date on the left side and a text field to enter an amount of hours in the middle and a submit button on the right   - DONE
2. User enters hours worked to associated date in the text field   - DONE
3. User presses the submit button  - DONE

Übersicht:  
1. User sees an overview over his amount worked associated to the specific date - DONE
2. User sees overtime/undertime highlighted - DONE

Analyse: - Scrapped Idea
1. User sees multiple charts  - Changed to single graphical chart and table variant for clarity - DONE
    2.1 Total hours worked     
        2.1.1 option to filter by week, month, year - DONE in Day by Day overview
    2.2 Overtime     
        2.2.1 Total overtime - DONE  
        2.2.2 Overtime occurence  
            2.2.2.1 Per Week of Year, Per Month of Year, Per Day of Week - Restricted to Daily, Monhtly and Yearly overview - DONE
   
![Flowchart](Hours\Images\Flowchart_Timetracker_Project.png)


