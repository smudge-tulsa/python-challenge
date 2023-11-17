#!/usr/bin/env python
# coding: utf-8

# import Pandas libraries
import pandas as pd

# Create a data frame from the css
df = pd.read_csv('election_data.csv')

# verify csv is read right and the data is clean & usable
df.head()
df.shape
df.info()

# calculate how many votes there were
votes = len(df)

# identify how many candidates there were
candidates = df.Candidate.unique()

# calculate how many votes each candidate received
canVotes = df['Candidate'].value_counts()

# calculate what each candidate's vote percentage was
per = df['Candidate'].value_counts(normalize=True).mul(100).round(3).astype(str) + '%'

# verify percentage calculations and save as a new data frame
dfPer = pd.DataFrame({'Candidate': candidates, 'Percentage': per})
dfPer

# Create the results data frame
dfStats = pd.DataFrame({'Candidate': candidates, 'Percentage': per, 'Count': canVotes})
dfStats.set_index('Candidate')
dfStats

# declare a winner based on the highest vote count
winner = df['Candidate'].value_counts().idxmax()

# print the results to screen
results = ("\n"
           "Election Results\n"
           "-------------------------\n"
           f"Total Votes: {votes}\n"
           "-------------------------\n"
           f"{dfStats}\n"
           "-------------------------\n"
           f"Winner: {winner}\n"
           "-------------------------\n"
)
print(results)

# output the results to 
with open('poll_results.txt', 'w') as f:
    f.write(results)

