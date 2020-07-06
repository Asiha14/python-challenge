import os
import csv

csvpath = os.path.join( 'Resources', 'election_data.csv')


with open(csvpath) as csvfile:

    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    votes = 0
    total = 0
    sub = 0
    candidates_names = []
    candidates = []
    date = []

    # Read each row of data after the header
    for row in csvreader:
        votes += 1
        candidates.append(row[2])
        if row[2] not in candidates_names:
            candidates_names.append(row[2])
        

    votecount = []
    votepercent = []
    i = 0

    for pol in candidates_names:
        votecount.append(candidates.count(pol))
        i +=1

    j = 0

    for v in votecount:
        percent = votecount[j]/votes
        votepercent.append(percent)
        j +=1

    winner = votecount.index(max(votecount))
        
    print("Election Results")
    print("----------------------")
    print(f"Total Votes: {votes}")
    print("----------------------")

    k = 0

    for pol in candidates_names:
        print(f"{candidates_names[k]}: {'{:.3%}'.format(votepercent[k])} ({votecount[k]})" )
        k += 1
    
    print("----------------------")
    print(f"Winner: {candidates_names[winner]}")
    print("----------------------")


analysispath = os.path.join('analysis')

os.chdir(analysispath)
L = ["Election Results \n","---------------------- \n",f"Total Votes: {votes} \n","---------------------- \n"]
K = ["---------------------- \n",f"Winner: {candidates_names[winner]} \n","----------------------"]
f= open("PyPollAnalysis.txt","w+")
f.writelines(L)


m = 0
for pol in candidates_names:
    f.write(f"{candidates_names[m]}: {'{:.3%}'.format(votepercent[m])} ({votecount[m]}) \n")
    m += 1

f.writelines(K)

f.close()

   