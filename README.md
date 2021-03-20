# Election Analysis with Python

## Project Overview
Seth and Tom have asked for a script to tally votes for a recent election. While we're determining who won the election, we will also analyze the data to provide the number of votes for each candidate and to tally how many votes came in from each county.

## Election Audit Results

### Where are the Votes Coming From?
The first question we want to answer is how many votes were cast in this election, and where did they come from?
![County_Votes](https://github.com/kaileymd/Election_Analysis/blob/main/Resources/County_Votes.png)

The script looks for each unique county, then counts how many votes belong to each one. To help us understand these numbers, it also calculates the percentage of each county turnout as part of the larger election.

Here we can see that **Denver** had the largest turnout, with 306,055 votes. That's an overwhelming 82.8% of the vote!

### Who Competed in the Election?
![Candidate_Votes](https://github.com/kaileymd/Election_Analysis/blob/main/Resources/Candidate_Votes.png)

Similarly to the process to determine the participating counties, the script also finds each unique candidate and counts how many votes belong to each one. Here we can see the candidate's name, followed by how many votes they received both as a percentage of the total vote and numerically.

### Final Election Results
The script publishes its findings to a text file, which displays the winner:
![Election_Results](https://github.com/kaileymd/Election_Analysis/blob/main/Resources/Election_Results.png)

For this election, the script shows Diana DeGette as the winner with 73.8% of the vote, or 272,892 votes out of the 369,711 total votes cast.

## Election Audit Summary
To apply this script to any election, I would need to make two main modifications:
- Change the file variables.
- Reconfigure the winning conditions depending on the style of election.

To use this script for more than one election, we would need to change the file input and output names. 
![Load_File](https://github.com/kaileymd/Election_Analysis/blob/main/Resources/Load_File.png)

If the file names stayed the same, they would overwrite each other and we would not be able to save them. Additionally, the script would *not* be able to perform its analysis if the files were named something else. This is a quick modification that would not take much time or training to do.

Since this script independently determines the number/names of candidates and counties, the script is very self-sufficient. With the file names taken into account, it could determine the winner for any election where the winner is the candidate with the most votes:
![Find_Winner](https://github.com/kaileymd/Election_Analysis/blob/main/Resources/Find_Winner.png)

However, not all elections are determined that way. For example, the presidential election is won using votes from the electoral college. If further calculations are needed to determine the winner by geography and assign a separate number of points, for example, the conditions for winning would need to be altered.
