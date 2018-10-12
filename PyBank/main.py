#Read the csv file
import os
import csv 

# Getting the csv file (data set)
csvFile = os.path.join('budget_data.csv')

# Creating a variable to store the data file
csvDataset = []
# Creating a variable to store the dates
csvDataset_Month = []
# Creating a variable to store the profits and losses
csvDataset_Amount = []

# Creating the line separators for the final summary print out
# Love this short cut, found it in "Learn Python the Hard Way"
lines = "-" * 25

# another way to call in a file without importing os "but then your team and TAs will hate you" -JM he he
# csvFile = "~/Documents/WashU_Bootcamp/Homework/budget_data.csv"

# Reading the file and for each row of data, adding it to the csvDataset list variables defined above
with open(csvFile,'r') as bankFile:
        csvRead = csv.reader(bankFile,delimiter=',')
        #print(csvRead)                                 # prints the bankFile
        csv_header = next(csvRead)                      # skips the header
        #print(f"CSV Header: {csv_header}")
        for row in csvRead:
            #print(row)
            csvDataset.append(row)                      # adding the row contents to the list
            csvDataset_Month.append(row[0])             # adding the first item (date) to a separate list using the index 0 (zero)
            csvDataset_Amount.append(int(row[1]))       # adding the second item (amount) to a separate list using the index 1 (one)
# I can see using a program to create my grocery list - 
# except I really like handwriting that list - threw this random thought in
# to make sure you're reading all these lovely comments ;P

# The total number of months included in the dataset using the length function
total_months = len(csvDataset_Month)

# The total net amount of "Profit/Losses" over the entire period
net_total = 0                                           # setting the initial variable amount to zero
for month, amount in csvDataset:                        # for the month and the amount in the dataset
    net_total += int(amount)                            # adding each amount to the net total variable

# The average change in "Profit/Losses" between months over the entire period
chgAmt = 0                                              # setting the initial variable to zero
monthChg = []                                           # creating ANOTHER list
for amount in range(1,len(csvDataset_Amount)):          # for each amount from row 1 to the end
    # Subtract the amount above from the amount below in the data set
    monthChg.append(csvDataset_Amount[amount] - csvDataset_Amount[amount-1])

chgAmt = round(sum(monthChg) / len(monthChg),2)         # calculating the average change over the entire period
# print(str(chgAmt))

# The greatest increase in profits (date and amount) over the entire period
# The greatest loss (date and amount) over the entire period
for amount in range(1,len(csvDataset_Amount)):          # for each amount from row 1 to the end
    maxIncr = max(monthChg)                             # getting the greatest increase using max function
    maxIncrIndex = monthChg.index(maxIncr)              # I did not yet understand the beauty of dictionaries
    maxDecr = min(monthChg)                             # getting the greatest decrease using min function
    maxDecrIndex = monthChg.index(maxDecr)              # had to get creative because I did not want to understand dictionaries yet

monthMaxIncr = csvDataset_Month[maxIncrIndex + 1]       # incrementing the index by 1 (one) since the first value in this list started with the second row
monthMaxDecr = csvDataset_Month[maxDecrIndex + 1]       # same - incrementing the index

# The final print out - Whoot!
print("Financial Analysis")
print(f"{lines}") 
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${chgAmt}")
print(f"Greatest Increase in Profits: {monthMaxIncr} (${maxIncr})")
print(f"Greatest Decrease in Profits: {monthMaxDecr} (${maxDecr})")

#  Write to a text file - got this from my friend, Learn Python the Hard Way / cross your fingers and pray this works!
target = open("pyBank.txt", 'w')
target.write("Financial Analysis\n")
target.write(f"{lines}\n") 
target.write(f"Total Months: {total_months}\n")
target.write(f"Total: ${net_total}\n")
target.write(f"Average Change: ${chgAmt}\n")
target.write(f"Greatest Increase in Profits: {monthMaxIncr} (${maxIncr})\n")
target.write(f"Greatest Decrease in Profits: {monthMaxDecr} (${maxDecr})\n")
# Yay, it works! As a CPA, I find the formatting to be horrendous, someone give me a comma for those numbers >= $1,000.00
# This was fun