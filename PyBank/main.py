# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. 

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
    #skip header row of data
    next(csvreader, None)
    
    #count the total months
    for row in csvreader:
        month += 1
#print(month) as check
        #compile dates as string in date list
        date.append(str(row[0]))
        #compile profit/loss data as an interger in profitloss list
        profitloss.append(int(row[1]))  
        
        #compile list of profit/loss changes month over month
        p_l = row[1] #setting variable 
        #calculate monthly change
        monthly_pl_change = int(p_l) - int(prev_month_profitloss)
        #compile monthly change in profitloss_change list
        profitloss_change.append(monthly_pl_change)
        #reset p_l variable to be the next pre_month_profitloss
        prev_month_profitloss = p_l     
        
# use define function to compute average change in profit/loss
#average = sum of profit loss change / number of months or length of profitloss change
def average(profitloss_change):
    monthlen = len(profitloss_change)
    #have to remove first value of profitloss change since there is no previous month
    #and reduce the count of the number of months by 1 from 86 to 85
    total = sum(profitloss_change) - profitloss_change[0] 
    #have to reduce of profitloss_change b/c first value makes no sense
    average_pl = total / (monthlen - 1)
    return average_pl

#calculate and store average change in profit/loss over the entire period
average_change = average(profitloss_change)
#print(average_change) test

#calculate and store net_profit/loss over the entire period
net_profitloss = sum(profitloss)
#print(net_profitloss) test

#find greatest increase and greatest decrease in change of profitloss along with corresponding months
#use max() min() to find max and min in profitloss_change
greatest_increase = max(profitloss_change)
greatest_decrease = min(profitloss_change)
#find the index number corresponding to the max and min
#use the index number to print corresponding date 
greatest_increase_month = profitloss_change.index(greatest_increase)
greatest_decrease_month = profitloss_change.index(greatest_decrease)

#print(date[greatest_increase_month])test


#print to terminal with f strings

print(f"Financial Analysis")
print(f"--------------------------")
print(f"Total Months: {month}")
print(f"Net Profit/Loss: ${net_profitloss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {date[greatest_increase_month]} $ {greatest_increase}")
print(f"Greatest Increase in Profits: {date[greatest_decrease_month]} $ {greatest_decrease}")

#create path to export file
output_path = os.path.join("..", "PyBank", "PyBank_Financial_Analysis.txt")
#create textfile (.txt)
with open("PyBank_Financial_Analysis.txt", 'w') as text_file:
  print(f"Financial Analysis", file=text_file)
  print(f"--------------------------", file=text_file)
  print(f"Total Months: {month}", file=text_file)
  print(f"Net Profit/Loss: ${net_profitloss}", file=text_file)
  print(f"Average Change: ${average_change}", file=text_file)
  print(f"Greatest Increase in Profits: {date[greatest_increase_month]} $ {greatest_increase}", file=text_file)
  print(f"Greatest Increase in Profits: {date[greatest_decrease_month]} $ {greatest_decrease}", file=text_file)


