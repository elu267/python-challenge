#Read the csv file
import os
import csv 

# Path to collect data from the Resources folder
# need to adjust this because the file is not 
# sitting in the PyBank folder

# getting the csv file (data set)
csvFile = os.path.join('budget_data.csv')

# another way to call in a file without importing os

#csvFile = "~/Documents/WashU_Bootcamp/Homework/budget_data.csv"
with open(csvFile,'r') as bankFile:
        csvRead = csv.reader(bankFile,delimiter=',')
        print(csvRead)

        csv_header = next(csvRead)
        print(f"CSV Header: {csv_header}")

        for row in csvRead:
            print(row)

#The total number of months included in the dataset

#The total net amount of "Profit/Losses" over the entire period

#The average change in "Profit/Losses" between months over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest loss (date and amount) over the entire period