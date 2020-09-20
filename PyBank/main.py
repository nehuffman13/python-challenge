#import 
import os
import csv

#enters variable definitions 
months = []
profit_loss = []
date_list = []

#creates start 
count_months = 0
profit_loss_total_change = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0


budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

#read csv

with open (budget_data_csv_path) as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

# reads through the rows of data 
for row in csv_reader:  
    count_months = 1
    
    if (count_months = 1) 
    previous_month_profit_loss = current_month_profit_loss
    continue
