### PROBLEM SET 3 INITIALIZATION AND DATA IMPORT (QUESTION 1-3)
import re

line_brk = "---------------------------------------------------------------------------------------------"
new_line = "\n"

# create link to data file
prob_set_3_file = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv')

# create empty dictionary to store data
dataDict = dict()

# for each line of the data that has a date and water level reading,
# save the water level into the dictionary with the date as the key
for line in prob_set_3_file:
    line = line.rstrip()
    date_waterLvl = re.findall('\d{4}-\d{2}-\d{2} \d{2}:\d{2},\d.\d{3}', line)
    
    if len(date_waterLvl) > 0:
        dateTime = re.findall('\d{4}-\d{2}-\d{2} \d{2}:\d{2}', date_waterLvl[0])
        waterLvl = re.findall('\d.\d{3}', date_waterLvl[0])
        
        dataDict[dateTime[0]] = float(waterLvl[0])

### QUESTION 1
print("QUESTION 1")
print(line_brk)

# saves the max water level value from the dictionary
max_waterLvl = max(dataDict.values())

# search the dictionary for the proper key/value that matches the saved max value
for key in dataDict:
    if dataDict[key] == max_waterLvl:
        print(f"The maximum water level is {max_waterLvl} and it occurred on {key}.")

print(new_line)

### QUESTION 2
print("QUESTION 2")
print(line_brk)

# saves the max, min, and sum of the water level values from the dictionary
max_waterLvl = max(dataDict.values())
min_waterLvl = min(dataDict.values())
sum_waterLvl = sum(dataDict.values())

# search the dictionary for the proper key/value that matches the saved max and min value
for key in dataDict:
    if dataDict[key] == max_waterLvl:
        print(f"The maximum water level is {max_waterLvl} and it occurred on {key}.")
    elif dataDict[key] == min_waterLvl:
        print(f"The minimum water level is {min_waterLvl} and it occurred on {key}.")
        
# calculate the average water level
avg_waterLvl = sum_waterLvl/len(dataDict.values())
print(f"The average water level is {avg_waterLvl}.")

print(new_line)

### QUESTION 3
print("QUESTION 3")
print(line_brk)

# save the first water level reading as the previous to avoid miscaluclating the water level change
prev_waterLvl = list(dataDict.values())[0]
maxChg_waterLvl = 0

# for each water level value, calculate the change from the previous stored reading
# if the newly calculated change is larger than the previous largest change, replace the stored max change
for key in dataDict:
    chg_waterLvl = (dataDict[key]) - (prev_waterLvl)
    
    if chg_waterLvl > maxChg_waterLvl:
        maxChg_waterLvl = chg_waterLvl
    
    prev_waterLvl = dataDict[key]
    
# reset the previous water level to the first value
prev_waterLvl = list(dataDict.values())[0]

# search the dictionary for the proper key/value that matches the saved max water level change
for key in dataDict:
    chg_waterLvl = (dataDict[key]) - (prev_waterLvl)
    
    if chg_waterLvl == maxChg_waterLvl:
        print(f"The maximum change in water level is {maxChg_waterLvl} and it occurred on {key}")
    
    prev_waterLvl = dataDict[key]

print(new_line)

### QUESTION 4
print("QUESTION 4")
print(line_brk)

# create link to data file
live_read = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv')

# line counter starts at -1 to account for the header line
lineCount = -1
prev_waterLvl = 0

# define a function to check for the given warning statements
# calculates the water level change and checks to see if it is > 0.25
# checks to see if the water level is > 5
def live_analysis(waterLvl):
    if ((waterLvl-prev_waterLvl) > 0.25):
        print(f"WARNING: The change in water level is {(waterLvl-prev_waterLvl)} (greater than 0.25).")
    if (waterLvl > 5):
        print(f"WARNING: The current water level is {waterLvl} (greater than 5).")

# reads each line of the data file
for line in live_read:
    line = line.rstrip()
    live_data = re.findall('\d{4}-\d{2}-\d{2} \d{2}:\d{2},\d.\d{3}', line)
    
    # checks if the line has a date and water level reading
    if len(live_data) > 0:
        lineCount += 1
        
        # saves the first water level reading to prev_waterLvl to avoid calculation errors
        if lineCount == 1:
            dateTime = re.findall('\d{4}-\d{2}-\d{2} \d{2}:\d{2}', live_data[0])[0]
            prev_waterLvl = float(re.findall('\d.\d{3}', live_data[0])[0])
            print(f"Data reading on {dateTime} is {prev_waterLvl}.")
            live_analysis(prev_waterLvl)
            print('\n')
        # checks each water level reading through the live_analysis function
        else:
            dateTime = re.findall('\d{4}-\d{2}-\d{2} \d{2}:\d{2}', live_data[0])[0]
            current_waterLvl = float(re.findall('\d.\d{3}', live_data[0])[0])
            print(f"Data reading on {dateTime} is {current_waterLvl}.")
            live_analysis(current_waterLvl)
            print('\n')
            
            prev_waterLvl = current_waterLvl
    # if a line does not have a water level reading, display proper warning
    else:
        lineCount += 1
        
        # prevents displaying warning for the header line
        if lineCount > 1:
            dateTime = re.findall('\d{4}-\d{2}-\d{2} \d{2}:\d{2}', line)[0]
            print(f"WARNING: No water level reading on {dateTime}")
            print('\n')