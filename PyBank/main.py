#!/usr/bin/env python
# coding: utf-8

# import libs & modules
import pandas as pd
from pathlib import Path

# create the data frame from the budget data CSV
df = pd.read_csv("budget_data.csv", parse_dates=["Date"], date_format='%d/%m/%y')
df.head()

# create a variable of the total change for the period (profit or loss)
total = df['Profit/Losses'].sum()
#total

# create a new column in df for daily change
df['change'] = df['Profit/Losses'].diff()
#df

# calculate the average daily change
avg = df['change'].mean()
#avg

# find the max change (i.e., the most profitable day)
max = df['change'].max()
#max

# find the min change (i.e., the biggest loss day)
min = df['change'].min()
#min

# find the date of the most profitable day
maxRow = df.loc[df['change'] == max]
maxDate = maxRow['Date']
#maxDate

# find the date of the biggest loss day
minRow = df.loc[df['change'] == min]
minDate = minRow['Date']
#minDate

# build a multi-line text variable to summarize the findings
analysis = ("\n"
            "Financial Analysis\n"
            "\n"
            "----------------------------\n"
            "\n"
            "Total Months: 86\n"
            "\n"
            f"Total: {total}\n"
            "\n"
            f"Average Change: {avg}\n"
            "\n"
            f"Greatest Increase in Profits: {maxDate} ({max})\n"
            "\n"
            f"Greatest Decrease in Profits: {minDate} ({min})\n")
#print(analysis)

# save the analysis to a txt file
with open('analysis.txt', 'w') as f:
    f.write(analysis)

