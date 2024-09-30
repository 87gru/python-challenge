"PyBank Script"

# Import csv and os modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Defining variables and lists
total_net = 0
total_months = 0
greatestincrease = 0    
greatestdecrease = 0
profitlosses = []
months = []
changes_in_profit = []


# Open and read the csv
with open(file_to_load, 'r') as financial_data:
    csvreader = csv.reader(financial_data,delimiter=',')

    # Skip the header row
    header = next(csvreader)

    # Extract Date into months list, extract Profits/Losses into profitlosses list
    # Add one for each row read into total_months, and add all values in Proft/Losses into total_net variable
    for row in csvreader:
        months.append(row[0])
        profitlosses.append(int(row[1]))
        total_net+= int(row[1])
        total_months+= 1


# Loop through profitlosses list, find the change in profit/loss for each month starting with Feb-10, append results to changes_in_profit list
for x in range(1,len((profitlosses))):
    changes_in_profit.append(int(profitlosses[x] - profitlosses[x-1]))


# Loop through changes_in_profit list to find largest/lowest numbers and their indices, add associated months to max/minmonth variables 
for x in changes_in_profit:
    if x > greatestincrease:
        greatestincrease = round(x)
        maxindex = changes_in_profit.index(x)
        maxmonth = months[maxindex+1] # +1 = row difference between total_months + changes_in_profit
    if x < greatestdecrease:
        greatestdecrease = round(x)
        minindex = changes_in_profit.index(x)
        minmonth = months[minindex+1]
    

# Calculate average of the changes in profits/losses
averagechange = round(sum(changes_in_profit) / len(changes_in_profit),2)


#Print output
print("\n")
print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: ${round(total_net)}\n")
print(f"Average Change: ${averagechange}\n")
print(f"Greatest Increase in Profits: {maxmonth} (${greatestincrease})\n")
print(f"Greatest Decrease in Profits: {minmonth} (${greatestdecrease})\n")



# Write the results that will be inputted into txt file
lines = ["","Financial Analysis","----------------------------",
f"Total Months: {total_months}",
f"Total: ${round(total_net)}",
f"Average Change: ${averagechange}",
f"Greatest Increase in Profits: {maxmonth} (${greatestincrease})",
f"Greatest Decrease in Profits: {minmonth} (${greatestdecrease})"]

#text file output
with open(file_to_output, "w") as txt:
    for line in lines:
        txt.write(str(f"{line}\n"))
        txt.write('\n')
