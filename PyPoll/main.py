#import
import os
import csv
import collections
from collections import Counter

election_data_csv_path = os.path.join("election_data.csv")

candidates = []
votes_total = 0
votes_per_candidates = []
months_count = 0

election_data_csv_path = os.path.join("Resources", "election_data.csv")

#open and read the csv 
with open (election_data_csv_path, newline="") as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    # Sort the list by default ascending order
    sorted_list = sorted(votes_total)
    
    # Arranges the sorted list 
    arrange_list = sorted_list

    #count votes per candidate 
    #most common order
    #appends to list
    count_candidate = Counter (arrange_list) 
    votes_per_candidates.append(count_candidate.most_common())

    # calculate the percentage of votes per candidate 
    for item in votes_per_candidates:
       
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourth = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')
