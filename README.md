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
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
