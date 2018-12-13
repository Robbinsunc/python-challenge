# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

#* Your task is to create a Python script that analyzes the records to calculate each of the following:

  # The total number of months included in the dataset

  #The total net amount of "Profit/Losses" over the entire period

 # The average change in "Profit/Losses" between months over the entire period

  # The greatest increase in profits (date and amount) over the entire period

  # The greatest decrease in losses (date and amount) over the entire period

# Import Modules    
import os
import csv
#define variables for counting months and profit/loss data
month = 0
date = []
profitloss = []
net_profitloss = 0
profitloss_change = []
prev_month_profitloss = 0

#Set path for file
pybank_csv = os.path.join("Resources", "budget_data.csv")

#Open csv file
with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    #count the total months
    for row in csvreader:
        month += 1
#print(month) as check
        date.append(str(row[0]))
        profitloss.append(int(row[1]))  
        
        #compile list of profit/loss changes month over month
        p_l = row[1]
        monthly_pl_change = int(p_l) - int(prev_month_profitloss)
        profitloss_change.append(monthly_pl_change)
        prev_month_profitloss = p_l     
        
#define function to compute average change in profit/loss
def average(profitloss_change):
    length = len(profitloss_change)
    total = sum(profitloss_change) - profitloss_change[0]
    #have to reduce of profitloss_change b/c first value makes no sense
    average_pl = total / (length - 1)
    return average_pl

#average change in profit/loss over the entire period
average_change = average(profitloss_change)

#net profit/loss over the entire period
net_profitloss = sum(profitloss)

#find greatest increase and greatest decrease along with corresponding months
greatest_increase = max(profitloss_change)
greatest_decrease = min(profitloss_change)
greatest_increase_month = profitloss_change.index(greatest_increase)
greatest_decrease_month = profitloss_change.index(greatest_decrease)


#print to terminal

print(f"Financial Analysis")
print(f"--------------------------")
print(f"Total Months: {month}")
print(f"Net Profit/Loss: ${net_profitloss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {date[greatest_increase_month]} $ {greatest_increase}")
print(f"Greatest Increase in Profits: {date[greatest_decrease_month]} $ {greatest_decrease}")

#create path to export file
output_path = os.path.join("..", "PyBank", "PyBank_Financial_Analysis.txt")

with open("PyBank_Financial_Analysis.txt", 'w') as text_file:
  print(f"Financial Analysis", file=text_file)
  print(f"--------------------------", file=text_file)
  print(f"Total Months: {month}", file=text_file)
  print(f"Net Profit/Loss: ${net_profitloss}", file=text_file)
  print(f"Average Change: ${average_change}", file=text_file)
  print(f"Greatest Increase in Profits: {date[greatest_increase_month]} $ {greatest_increase}", file=text_file)
  print(f"Greatest Increase in Profits: {date[greatest_decrease_month]} $ {greatest_decrease}", file=text_file)


