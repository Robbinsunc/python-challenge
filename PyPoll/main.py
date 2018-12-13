## PyPoll

# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
#(Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't 
#what it used to be.)

# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
#The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
#Your task is to create a Python script that analyzes the votes and calculates each of the following:

#The total number of votes cast

# A complete list of candidates who received votes

#The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.


#Import Modules    
import os
import csv

#define variables from data set election_data.csv
candidate_names = []
total_votes = 0
vote_count = []

#Set path for file
election_csv = os.path.join("Resources", "election_data.csv")

#Open csv file
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    #get total votes and rename row[2] as name
    for row in csvreader:
        total_votes += 1
        name = row[2]
        #build candidate_names and vote_count lists
        if name not in candidate_names:
            candidate_names.append(name)
            vote_count.append(1)
        else:
            candidate = candidate_names.index(name)
            vote_tally = vote_count[candidate]
            vote_count[candidate] = vote_tally + 1
#print(candidate_names)
#print(vote_count)

most_votes = 0
percent = []

for ind_votes in range(len(candidate_names)):
        ind_percent = vote_count[ind_votes]/total_votes * 100
        percent.append(ind_percent)
        
        if vote_count[ind_votes] > vote_count[0]:
            vote_count[0] = vote_count[ind_votes]
        winner = candidate_names[most_votes]
#print(winner)

#print results
print("Election Results")
print("-------------------------------")
print(f"Total Votes: {total_votes}")
for ind_votes in range(len(candidate_names)):
    print(f"{candidate_names[ind_votes]}: {percent[ind_votes]}% ({vote_count[ind_votes]})")
print("--------------------------------")
print(f"Winner: {winner}")

#create path to export file
output_path = os.path.join("..", "PyPoll", "PyPoll_Election_Results.txt")

with open ("PyPoll_Election_Results.txt", "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    for ind_votes in range(len(candidate_names)):
        print(f"{candidate_names[ind_votes]}: {percent[ind_votes]}% ({vote_count[ind_votes]})", file=text_file)
    print("--------------------------------", file=text_file)
    print(f"Winner: {winner}", file=text_file)

