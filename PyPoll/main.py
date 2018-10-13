# Read the csv file
import os
import csv

# getting the csv file (data set)
csvFile = os.path.join('election_data.csv')

# creating a variable to store the entire dataset
csvDataset = []
# creating a variable to store the candidate names
csvDataset_Candidate = []
# creating a variable to store the voter IDs
csvDataset_VoterID = []
# creating a variable to hold the candidate, percentage of votes and total votes
summary_votes = []
# creating formatting for print
lines = "-" * 25

# another way to call in a file without importing os is using pandas - holy cow, that is so much simpler
with open(csvFile,'r') as electionFile:
        csvRead = csv.reader(electionFile,delimiter=',')
        #print(csvRead)
        csv_header = next(csvRead)                      #skips the header
        #print(f"CSV Header: {csv_header}")
        for row in csvRead:
            # print(row)
            # this creates a list of dictionaries (i.e. one dictionary for each voter ID)
            # you missed a great white boarding session as I figured this out
            # adds the keys for the header and selects each value by its index
            csvDataset.append({
            'voterID': row[0], \
            'county': row[1], \
            'candidate': row[2]
            })
            csvDataset_Candidate.append(row[2])             # giving myself list options for later
            csvDataset_VoterID.append(row[0])               # same

# the total number of votes cast
total_votes = len(csvDataset_VoterID)
# a complete list of candidates who received votes
unique_candidate = []
def unique():
    # global allows write access to the list variable, unique_candidate
    global unique_candidate     
    #loop through all elements in list
    for x in csvDataset_Candidate:
        # check if candidate exists in the unique list or not
        if x not in unique_candidate:
            unique_candidate.append(x)
    #for x in unique_candidate:
        #print(x)

# calling the function because if you don't then nothing happens
unique()

# the percentage of votes each candidate won
# the total number of votes each candidate won
def sumVotes():
    for z in unique_candidate:                      # z becomes the candidate name  
        votes = 0                                   # variable resets to zero each loop   
        #print(z)   
        for c in csvDataset:                        # c is the counter that loops through the dictionary
            if z == c["candidate"]:                 # because z always equals c (duh) - see vba homework
                votes += 1                          # tally of votes per candidate
        #print(votes)
        pctVotes = round(((votes/total_votes) * 100), 3)     # calculating the percentage of votes with three decimals
        # adding each key and value to a dictionary
        summary_votes.append({'candidate': z,'pctVotes': pctVotes, 'totVotes': votes})

sumVotes()                                          # calling the function
#print(summary_votes)                                

# the winner of the election based on popular vote 
winnerChickenDinner = None                          # setting variable to no one
def winner():
    rockTheVote = 0                                 # setting variable to zero
    global winnerChickenDinner                      # made this global b/c it wouldn't print otherwise
    for x in summary_votes:                         # looping through total votes in the dictionary
        if x['totVotes'] > rockTheVote:             # if the value is the maximum then that is the winner
            rockTheVote = x['totVotes']             # getting and storing max votes
            winnerChickenDinner = x['candidate']    # the name of the winner if they have the max votes

winner()

print("Election Results\n")
print(f"{lines}\n")
print(f"Total Votes: {total_votes}\n")
print(f"{lines}\n")
for x in summary_votes:
    print("{0}: {1:.3f}% ({2:.0f})\n".format(x['candidate'], x['pctVotes'], x['totVotes']))
print(f"{lines}\n")
print(f"Winner: {winnerChickenDinner}\n")
print(f"{lines}")

#  Write to a text file
target = open("pyPoll.txt", 'w')

target.write("Election Results\n")
target.write(f"{lines}\n")
target.write(f"Total Votes: {total_votes}\n")
target.write(f"{lines}\n")
for x in summary_votes:
    target.write("{0}: {1:.3f}% ({2:.0f})\n".format(x['candidate'], x['pctVotes'], x['totVotes']))
target.write(f"{lines}\n")
target.write(f"Winner: {winnerChickenDinner}\n")
target.write(f"{lines}")