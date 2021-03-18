#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

#Import modules

import os
import csv

#Assign a variable for the file to load and the path.
file_to_load = "Resources/election_results.csv"

#Filename variable to a direct or indirect path to file
# file_to_save = os.path.join("analysis", "election_analysis.txt")

#write data to the txt file using open()
# with open(file_to_save, "w") as txt_file:

    #write header
    # txt_file.write("Counties in the Election\n------------------------\n")
    #write data to the file
    # txt_file.write("Arapahoe\nDenver\nJefferson")

#Initialize total vote counter
total_votes = 0

#Initialize new list
candidate_options = []

#Initialize new dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: read and analyze data
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #Add unique name to options list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #Begin tracking unique candidate vote count
            candidate_votes[candidate_name] = 0
        
        #Add votes to initial candidate vote count
        candidate_votes[candidate_name] += 1
    
    #Iterate through candidate list
    for candidate_name in candidate_votes:

        #Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        #Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #To do: Print candidate name and percentage of votes
        # print(f"{candidate_name}: received {votes}, which is {vote_percentage:.1f}% of the vote.")

        #Determine winning vote count and candidate
        #Are votes > winning count?
        
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            #If true, set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            #Set winning_candidate equal to candidate's name
            winning_candidate = candidate_name
    
        #Print winning candidate, vote count, and percentage
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #Print winning_candidate_summary
    winning_candidate_sumary = (
        f"----------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------\n")
        
    print(winning_candidate_sumary)