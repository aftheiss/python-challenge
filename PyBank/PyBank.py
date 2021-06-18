import os
import csv
import statistics

PyBankData = os.path.join("Resources/budget_data.csv")



# Lists to store data
Total_Months = []
Total_Net = []
Average_Changes = []
GreatestIncreaseAmount = []
GreatestDecreaseAmount = []


# open
with open(PyBankData, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader, None)

    for row in csvreader:
       
        # Add Total Months
        Total_Months.append(row[0])
       
        # Total Net Price
        Total_Net.append(int(row[1]))
    
    # average change
    for x in range(len(Total_Net)-1):
        Average_Changes.append(Total_Net[x+1]-Total_Net[x])

       
       
        GreatestIncrease = max(Average_Changes)
        GreatestDecrease = min(Average_Changes)


# Get the min/max change
GreatestIncreaseAmount = (Average_Changes.index(GreatestIncrease)) + 1
GreatestDecreaseAmount = (Average_Changes.index(GreatestDecrease)) + 1 

number_of_months = len(Total_Months)
sum_total = sum(Total_Net)

# Print loop info
print("Financial Analysis")
print("==========================")
print(f"Total Months: {number_of_months}")
print(f"Total: {sum_total}")
print(f"Average Change: {round(sum(Average_Changes)/len(Average_Changes),2)}")
print(f"Greatest Increase: {Total_Months[GreatestIncreaseAmount]} (${((GreatestIncrease))})")
print(f"Greatest Decrease: {Total_Months[GreatestDecreaseAmount]} (${((GreatestDecrease))})")


# export,  print & add line break
output_file = os.path.join("Analysis/FinalResults.txt") 

with open(output_file, "w") as Results:

    Results.write( "Financial Analysis\n"
"==========================\n"
f"Total Months: {number_of_months}\n"
f"Total: {sum_total}\n"
f"Average Change: {round(sum(Average_Changes)/len(Average_Changes),2)}\n"
f"Greatest Increase: {Total_Months[GreatestIncreaseAmount]} (${((GreatestIncrease))})\n"
f"Greatest Decrease: {Total_Months[GreatestDecreaseAmount]} (${((GreatestDecrease))})\n"
                   
)