#Read the csv file
import os
import csv 

# Path to collect data from the Resources folder
# need to adjust this because the file is not 
# sitting in the PyBank folder

# getting the csv file (data set)
csvFile = os.path.join('budget_data.csv')

# creating a variable to store the data file
csvDataset = []
# creating a variable to store the dates
csvDataset_Month = []
# creating a variable to store the profits and losses
csvDataset_Amount = []

# creating the line separators for the print out
lines = "-" * 25

# another way to call in a file without importing os
#csvFile = "~/Documents/WashU_Bootcamp/Homework/budget_data.csv"
with open(csvFile,'r') as bankFile:
        csvRead = csv.reader(bankFile,delimiter=',')
        print(csvRead)
        csv_header = next(csvRead)                      #skips the header
        print(f"CSV Header: {csv_header}")
        for row in csvRead:
            print(row)
            csvDataset.append(row)
            csvDataset_Month.append(row[0])
            csvDataset_Amount.append(int(row[1]))

#The total number of months included in the dataset
total_months = len(csvDataset_Month)

#The total net amount of "Profit/Losses" over the entire period
net_total = 0
for month, amount in csvDataset:
    net_total += int(amount)

#The average change in "Profit/Losses" between months over the entire period
chgAmt = 0
monthChg = []
for amount in range(1,len(csvDataset_Amount)):
    # subtract the amount above from the amount below in the data set
    monthChg.append(csvDataset_Amount[amount] - csvDataset_Amount[amount-1])

chgAmt = round(sum(monthChg) / len(monthChg),2)
print(str(chgAmt))

#The greatest increase in profits (date and amount) over the entire period
#The greatest loss (date and amount) over the entire period
for amount in range(1,len(csvDataset_Amount)):
    maxIncr = max(monthChg)
    maxIncrIndex = monthChg.index(maxIncr)
    maxDecr = min(monthChg)
    maxDecrIndex = monthChg.index(maxDecr) 

monthMaxIncr = csvDataset_Month[maxIncrIndex + 1]
monthMaxDecr = csvDataset_Month[maxDecrIndex + 1]

#The final print out
print("Financial Analysis")
print(f"{lines}") #This is so cool, found it in "Learn Python the Hard Way"
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${chgAmt}")
print(f"Greatest Increase in Profits: {monthMaxIncr} (${maxIncr})")
print(f"Greatest Decrease in Profits: {monthMaxDecr} (${maxDecr})")

# export results to text file
