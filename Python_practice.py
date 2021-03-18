# counties = ["Arapahoe","Denver","Jefferson"]

# counties_dict = {"Arapahoe": 422829, "Denver":463353, "Jefferson": 432468}

# for county, voters in counties_dict.items():
        # print(county, "county has", voters, "registered voters.")
        # print(f"{county} county has {voters} registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]


for county_dict in voting_data:
        county = county_dict["county"]
        voters = county_dict["registered_voters"]
        print(f"{county} county has {voters} registered voters.")






        # county = county_dict.values()
        # for key in county_dict:
        #         print(county_dict[key])

# print(countyname, numbervoters)

# for county_dict in voting_data:
        # print(f"{county} county has {vote_count} registered voters.")

# candidate_votes = int(input("How many votes did the cadidate get in the election?"))

# total_votes = int(input("What is the toal number of votes in the elction?"))

# message_to_candidate = (
        # f"You received {candidate_votes} number of votes."
        # f"The total number of votes in the election was {total_votes}."
        # f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes."
# )
# print(message_to_candidate)

