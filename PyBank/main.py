import os
import csv

csvpath = os.path.join( 'Resources', 'budget_data.csv')

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contentsactivate PythonData
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    mon = 0
    total = 0
    
    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        mon += 1
        total += int(row[1])
  
    
    average = round((total/mon),2)
    print(f"Financial Analysis")
    print(f"----------------------")
    print(f"Total Months: {mon}")
    print(f"Total: ${total}")
    #print(f"Average  Change: ${average}")
   
    r = [hrow for idx, hrow in enumerate(cvsreader) if idx in (28,62)]
    print(r)