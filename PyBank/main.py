import os
import csv

csvpath="Resources/budget_data.csv"

# Initial Values for Greatest Increase/Decrease in Loss/Profit over entire period:
Greatest_Increase=0
Greatest_Decrease=0

with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    # Header:
    csv_header = next(csvreader)

    # Information about the first Month
    csv_First_Month=next(csvreader)
    First_Amount=float(csv_First_Month[1])

    # Starting Value for Total Amount before entering the for loop:
    Total_Amount=First_Amount

    # Initial Value to determine the change in loss/profit:
    New_Amount=First_Amount

    # Starting point for Total Months
    Total_Months=1

    for row in csvreader:
        # The total number of months included in the dataset:
        Total_Months=Total_Months+1
        # The net total amount of "Profit/Losses" over the entire period
        Total_Amount=Total_Amount+float(row[1])      
        
        # The Last Profit/Losses on the Dataset:

        Last_Amount=float(row[1])

        # The greatest increase/decrease in profits (date and amount) over the entire period
        if Total_Months >= 2:
            Old_Amount=New_Amount
            New_Amount=float(row[1])
            change=New_Amount-Old_Amount
            # The greatest increase in profits (date and amount) over the entire period
            if change>Greatest_Increase:
                Greatest_Increase=change
                Greatest_Increase_Date=row[0]
            # The greatest decrease in losses (date and amount) over the entire period
            if change<Greatest_Decrease:
                Greatest_Decrease=change
                Greatest_Decrease_Date=row[0]

    # The average of the changes in "Profit/Losses" over the entire period
    Average_Change=(Last_Amount-First_Amount)/(Total_Months-1)
    Average_Change=round(Average_Change,2)

# Print out the results:
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total_Amount}")
print(f"Average Change: {Average_Change}")
print(f"Greatest Increase in Profits: {Greatest_Increase_Date} ({Greatest_Increase})")
print(f"Greatest Decrease in Profits: {Greatest_Decrease_Date} ({Greatest_Decrease})")

# Export a text file with the results.
output_path=os.path.join("new.txt")

with open(output_path, 'w', newline='') as txtfile:
    txtfile.write("Financial Analysis \n") 
    txtfile.write("---------------------------- \n")
    txtfile.write(f"Total Months: {Total_Months} \n")
    txtfile.write(f"Total: ${Total_Amount} \n")
    txtfile.write(f"Average Change: {Average_Change} \n")
    txtfile.write(f"Greatest Increase in Profits: {Greatest_Increase_Date} ({Greatest_Increase}) \n")
    txtfile.write(f"Greatest Decrease in Profits: {Greatest_Decrease_Date} ({Greatest_Decrease}) \n")
