import os
import csv

csvpath = os.path.join( 'Resources', 'budget_data.csv')


with open(csvpath) as csvfile:

    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    mon = 0
    total = 0
    sub = 0
    Changes = []
    date = []

    # Read each row of data after the header
    for row in csvreader:
        mon += 1
        total += int(row[1])
        profit = int (row[1])
        change = profit-sub
        Changes.append(change)
        sub = profit
        date.append(row[0])
    Changes.pop(0)
    date.pop(0)
    average = round(sum(Changes)/(mon-1),2)
    maxdate = Changes.index(max(Changes))
    mindate = Changes.index(min(Changes))
    
    
    print("Financial Analysis")
    print("----------------------")
    print(f"Total Months: {mon}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {date[maxdate]} (${max(Changes)})")
    print(f"Greatest Decrease in Profits: {date[mindate]} (${min(Changes)})")

analysispath = os.path.join('analysis')

os.chdir(analysispath)
L = ["Financial Analysis \n","---------------------- \n",f"Total Months: {mon} \n",f"Total: ${total} \n",f"Average Change: ${average} \n",
f"Greatest Increase in Profits: {date[maxdate]} (${max(Changes)}) \n", f"Greatest Decrease in Profits: {date[mindate]} (${min(Changes)})"]

f= open("PyBankAnalysis.txt","w+")
f.writelines(L)
f.close()