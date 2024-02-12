import os
import csv
import pandas as pd

csvpath = os.path.join('.','Resources', 'election_data.csv')

print(csvpath)


# # Read and print the contents of the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    #[print(row) for row in csvreader].head()

# Read the dataset into a pandas DataFrame
df = pd.read_csv(csvpath)

# Calculate the total number of votes cast
total_votes = df['Ballot ID'].count()
print(f'The total number of votes cast in {csvpath} is: {total_votes}')
# Get a list of unique candidates who received votes
candidates = df['Candidate'].unique()

# Print the list of candidates
print("List of candidates who received votes:")
for candidate in candidates:
    print(candidate)

# Calculate the percentage of votes each candidate won
candidate_votes = df['Candidate'].value_counts()
candidate_percentages = (candidate_votes / total_votes) * 100

# Print the percentage of votes each candidate won
print("Percentage of votes each candidate won:")
for candidate, percentage in candidate_percentages.items():
    print(f"{candidate}: {percentage:.2f}%")

# Count the total number of votes each candidate won
candidate_votes = df['Candidate'].value_counts()

# Print the total number of votes each candidate won
print("Total number of votes each candidate won:")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes} votes")

# Find the winner (candidate with the most votes)
winner = candidate_votes.idxmax()

# Print the winner of the election
print(f"The winner of the election based on popular vote is: {winner}")

# Write results to text file
print("Election Results")
print(f"Total Votes: {total_votes}")
print("Total number of votes each candidate won:")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes} votes ({candidate_percentages[candidate]:.2f}%)")
print(f"The winner of the election is: {winner}")  