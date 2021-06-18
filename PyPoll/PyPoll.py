
import os
import csv
import statistics

# Path for csv data
PyPollData = os.path.join("Resources/election_data.csv")

# Declare Variables for votes starting at 0
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv 
with open(PyPollData, newline='') as csvfile:

    # Store
    csvreader = csv.reader(csvfile,delimiter=",") 

    # Skip the header
    header = next(csvreader)     

    # go through each row after header
    for row in csvreader: 

        # Count through the unique voters
        total_votes +=1

        # Separate count for each individual
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 # used a dict to find a winner
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# using a max function of the dict/key to find a winner
dict_key = dict(zip(candidates,votes))
key = max(dict_key, key=dict_key.get)

# Print a the summary of the analysis
khan_percent = (khan_votes/total_votes) * 100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes) * 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print the summary table
print(f"----------------------------")
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")

# export print and add in line break
output_file = os.path.join("Analysis/FinalResults.txt") 

with open(output_file, "w") as Results:

    Results.write(f"----------------------------\n"
                  f"Election Results\n"
                  f"----------------------------\n"
                  f"Total Votes: {total_votes}\n"
                  f"----------------------------\n"
                  f"Khan: {khan_percent:.3f}% ({khan_votes})\n"
                  f"Correy: {correy_percent:.3f}% ({correy_votes})\n"
                  f"Li: {li_percent:.3f}% ({li_votes})\n"
                  f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})\n"
                  f"----------------------------\n"
                  f"Winner: {key}\n"
)
