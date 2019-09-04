import os
import csv

csvpath="Resources/election_data.csv"

# Initial Value of total number of votes cast:
num_votes=0
# A complete list of candidates who received votes:
Candidates=[]
# The total number of votes each candidate won:
votes_per_candidate=[]

with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    # Header:
    csv_header=next(csvreader)

    for row in csvreader:
        # The total number of votes cast:
        num_votes=num_votes+1

        if row[2] not in Candidates:
            Candidates.append(row[2])
            votes_per_candidate.append(0)
        
        votes_per_candidate[Candidates.index(row[2])]=votes_per_candidate[Candidates.index(row[2])]+1

# Index of the winner:
winner=votes_per_candidate.index(max(votes_per_candidate))

# Print Results:
print("Election Results")
print("-------------------------")
print(f"Total Votes: {num_votes}")
print("-------------------------")

for i in range(int(len(Candidates))):
    # The percentage of votes each candidate won
    voter_percentage=round(votes_per_candidate[i]/num_votes*100,3)
    print(f"{Candidates[i]}: {voter_percentage}% ({votes_per_candidate[i]})")

print("-------------------------")
print(f"Winner: {Candidates[winner]}")
print("-------------------------")

# Export a text file with the results
output_path=os.path.join("new.txt")
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write("Election Results \n") 
    txtfile.write("------------------------ \n") 
    txtfile.write(f"Total Votes: {num_votes} \n")
    txtfile.write("------------------------ \n") 

    for i in range(int(len(Candidates))):
        # The percentage of votes each candidate won
        voter_percentage=round(votes_per_candidate[i]/num_votes*100,3)
        txtfile.write(f"{Candidates[i]}: {voter_percentage}% ({votes_per_candidate[i]}) \n")
    
    txtfile.write("------------------------ \n") 
    txtfile.write(f"Winner: {Candidates[winner]} \n")
    txtfile.write("------------------------ \n") 
