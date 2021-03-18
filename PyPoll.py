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
file_to_save = os.path.join("analysis", "election_analysis.txt")

#write data to the txt file using open()
with open(file_to_save, "w") as txt_file:

    #write header
    txt_file.write("Counties in the Election\n------------------------\n")
    #write data to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")

#Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: read and analyze data
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)

    #Print each row in the CSV file.
    # for row in file_reader:
        # print(row)