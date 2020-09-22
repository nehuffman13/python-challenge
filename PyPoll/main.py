# importing data 
import os
import csv
import collections
from collections import Counter

election_data_csv_path = os.path.join("election_data.csv")

# variable definitions
candidates = []
votes_total = 0
votes_per_candidates = []
months_count = 0
percentage_of_votes = []

# path for data 
election_data_csv_path = os.path.join("Resources", "election_data.csv")


    #open and read the csv 
with open (election_data_csv_path, newline="") as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csv_reader:
        votes_per_candidates.append(row[2])

    # Sort the list by default ascending order
    sorted_list = sorted(votes_per_candidates)
    
    # Arranges the sorted list 
    arrange_list = sorted_list

    #count votes per candidate 
    #most common order
    #appends to list
    count_candidate = Counter (arrange_list) 
    votes_per_candidates.append(count_candidate.most_common())


print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print(f"{votes_per_candidates[0][0][0]}")
print(f"{votes_per_candidates[0][1][0]}")
print(f"{votes_per_candidates[0][2][0]}")
print(f"{votes_per_candidates[0][3][0]}")
