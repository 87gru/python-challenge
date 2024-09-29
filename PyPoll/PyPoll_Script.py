"PyPoll Script"

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Set variables and lists
total_votes = 0  
candidate = []
vote_count = []
vote_percent = []


# Open the CSV file
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset: add vote to total_votes. Conditional statement to add candidates to list and count their votes
    for row in reader:
        total_votes+=1
        if row[2] not in candidate:
            candidate.append(row[2]) # Add name to candidate list
            vote_count.append(1) # Append integer value of 1 to vote_count list
        elif row[2] in candidate:
            index = candidate.index(row[2]) # Get index value of candidate in candidate list
            vote_count[index]+= 1 # Add vote to index that matches candidate index in candidate list


# Set variables to winner and percent calculations
winnercount = 0
percent_calc = 0

# Loop through vote_count list and calculate percentage, then append to vote_percent list. Conditional statement to define winner and highest vote count
for votes in vote_count:
    percent_calc = round(((votes / total_votes) * 100),3)
    vote_percent.append(percent_calc)
    if votes > winnercount:
        winnercount = votes
        index = vote_count.index(votes)
        winner = candidate[index]

# Print results to console
print("")
print("Election Results\n")
print("----------------------------\n")
print(f"Total Votes: {total_votes}\n")
print("----------------------------\n")
for x in range(len(candidate)):
    print(f"{candidate[x]}: {vote_percent[x]}% ({vote_count[x]})\n")
print("----------------------------\n")
print(f"Winner: {winner}\n")
print("----------------------------\n")



# Text file ouput into lists
txtlist1 = ["","Election Results","----------------------------",f"Total Votes: {total_votes}","----------------------------"]
candidate_results = [f"{candidate[x]}: {vote_percent[x]}% ({vote_count[x]})" for x in range(len(candidate))]
txtlist2 = ["----------------------------",f"Winner: {winner}","----------------------------"]

# Write text file
with open(file_to_output, "w") as txt_file:
    for t in txtlist1:
        txt_file.write(str(f"{t}\n"))
        txt_file.write('\n') 
    for can in candidate_results:
        txt_file.write(str(f"{can}\n"))
        txt_file.write('\n')
    for t in txtlist2:
        txt_file.write(str(f"{t}\n"))
        txt_file.write('\n') 
