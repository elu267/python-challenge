#Read the csv file
import os
import csv 

# Path to collect data from the Resources folder
# need to adjust this because the file is not 
# sitting in the PyBank folder

# getting the csv file (data set)
csvFile = os.path.join('election_data.csv')

# creating a variable to store the entire data file in a dictionary
csvDataset = []
# creating a variable to store the candidate names
csvDataset_Candidate = []
# creating a variable to store the voter IDs
csvDataset_VoterID = []

# creating formatting for print
lines = "-" * 25

# another way to call in a file without importing os
#csvFile = "~/Documents/WashU_Bootcamp/Homework/election_data.csv"
with open(csvFile,'r') as electionFile:
        csvRead = csv.reader(electionFile,delimiter=',')
        print(csvRead)
        csv_header = next(csvRead)                      #skips the header
        print(f"CSV Header: {csv_header}")
        for row in csvRead:
            #print(row)
            csvDataset.append({
            'voterID': row[0], \
            'county': row[1], \
            'candidate': row[2]
            })
            csvDataset_Candidate.append(row[2])
            csvDataset_VoterID.append(row[0])
            

# the total number of votes cast
total_votes = len(csvDataset_VoterID)
# a complete list of candidates who received votes
unique_candidate = []
def unique(csvDataset_Candidate):
    global unique_candidate
    #loop through all elements in list
    for x in csvDataset_Candidate:
        # check if candidate exists in the unique list or not
        if x not in unique_candidate:
            unique_candidate.append(x)
    for x in unique_candidate:
        print(x)

unique(csvDataset_Candidate)

# the percentage of votes each candidate won

# the total number of votes each candidate won

# the wnner of the election based on popular vote

print("Election Results")
print(f"{lines}")
print("Total Votes: {total_votes}")
print(f"{lines}")
print(f"{unique_candidate[0]}")
print(f"{unique_candidate[1]}")
print(f"{unique_candidate[2]}")
print(f"{unique_candidate[3]}")