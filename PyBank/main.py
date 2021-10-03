import os
import csv

#object from CSV file
budget_data = os.path.join("budget_data.csv")

total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#Open/Read csv file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvreader)
    
    #1st row to trak changes
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    for row in csvreader:
        
        dates.append(row[0])

        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months += 1

        #Total net amount of "Profit/Losses over entire period"
        total_pl = total_pl + int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease (lowest increase) in profits
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    

#Create Financial Analysis output
FAnalysisOutput = (f"Financial Analysis\n"
                   f"---------------------------\n"
                   f"Total Months: {len(Dates)}\n"
                   f"Average Change: ${AverageChange}\n"
                     f"Greatest Increase in Profits: {GIdate} (${GreatestIncrease})\n"
                  f"Greatest Decrease in Profits: {GDdate} (${GreatestDecrease})\n"
)

print(analysisOutput)

with open(outputfile, 'w') as textfile:
    textfile.write(analysisOutput)
