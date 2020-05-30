#!/usr/bin/env python
# coding: utf-8

# In[40]:


import os
import csv

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Challenge County names and county votes
county_name = []
county_options = []
county_votes = {}

# Challenge largest county name and metrics 
lcounty = ""
lcounty_votes = 0



# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row. 
    headers = next(file_reader)
   
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1 
        
        # Print the candidate name from each row.
        candidate_name = row[2]
        
        # get county name from each row
        county_name = row[1]

        #logic, if candidate doesn't match then add him to the list
        if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count. start at 0
            candidate_votes[candidate_name] = 0
        # else add candidate vote each time when candidate name matches    
        candidate_votes[candidate_name] += 1 
        
        # Challenge objective
        # if county name is not already there, add it
        if county_name not in county_options: 
            county_options.append(county_name)
            
            #begin tracking county votes initialize with 0 
            county_votes[county_name] = 0
        #add up county votes when it matches    
        county_votes[county_name] +=1
    
    # challenge objective 
    # for loop all counties 
with open(file_to_save, "w") as txt_file:
    for county in county_votes: 
        #figure out county vote count and percentages
        county_vote = county_votes[county]
        county_percent = int(county_vote)/int(total_votes) *100
        
        county_results = (
            f"{county}: {county_percent:.1f}% ({county_vote:,})\n")
        print(county_results, end="")
        txt_file.write(county_results)
        
        # challenge determin winning county 
        if (county_vote > lcounty_votes):
            lcounty_votes = county_vote
            lcounty = county

    #print the county with the largest turnout
    lcounty = (
        f"\n------------------\n"
        f"Largest County turn out is: {lcounty}\n"
        f"\n------------------\n")

    print(lcounty)
    txt_file.write(lcounty)
    
 
            
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    # Print the candidate vote dictionary.
  #  print(candidate_votes)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
       # print(f"{candidate}: received  {vote_percentage:.1f}% of the vote.")        

        # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    #    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
             # 2. If true then set winning_count = votes and winning_percent =
             # vote_percentage.
             winning_count = votes
             winning_percentage = vote_percentage
             # 3. Set the winning_candidate equal to the candidate's name.
             winning_candidate = candidate  
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
    

