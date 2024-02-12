#import necessary modules
import os
import csv
from datetime import datetime

#Define the csv path
csvpath = os.path.join('.','Resources', 'budget_data.csv')
print(csvpath)

#Read and print the csv contents
with open (csvpath) as csvfile:
    #create a csv reader project
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #iterate through each row in the CSV file and print
    for row in csvreader:
        print(row)

#Define a function to count the number of months
def count_months(csv_file_path):

    with open(csv_file_path, 'r') as csvfile:
        # Initialize month count
        month_count = 0
       
        # Create a CSV reader object
        reader = csv.reader(csvfile)
        header = next(reader)
         
         # Iterate through each row and count
        for row in reader:
            month_count = month_count + 1
           
    return month_count

# Call the count_months function and print the result
csv_file_path = csvpath
total_months = count_months(csvpath)

print(f'Total number of months: {total_months}')

#SDefine a function to calculate changes and average
def calculate_changes_and_average(csv_file_path):
    changes = []
    total_profit_losses = 0
    total_months = 0

    with open(csv_file_path, 'r') as csvfile:
         
         # Create a CSV reader object with a header
        reader = csv.DictReader(csvfile)
        previous_profit_losses = None
         
         # Iterate through each row
        for row in reader:
            date = row['Date']
            profit_losses = int(row['Profit/Losses'])
         # Update total profit/losses 
            total_profit_losses += profit_losses
         # Calculate and store changes   total_months += 1

            if previous_profit_losses is not None:
                change = profit_losses - previous_profit_losses
                changes.append(change)

            previous_profit_losses = profit_losses

    # Calculate the average change
    average_change = sum(changes) / len(changes)

    return changes, average_change, total_months, total_profit_losses

# Call and print 
csv_file_path = csvpath
changes, average_change, total_months, total_profit_losses = calculate_changes_and_average(csv_file_path)

print(f'Total Months: {total_months}')
print(f'Total Profit/Losses: ${total_profit_losses}')

#print(f'Changes in Profit/Losses: {changes}')
print(f'Average Change: ${average_change:.2f}')  

#Define a function to find the greatest profit increase
def greatest_profit_increase(csv_file_path):
    max_increase = 0
    max_increase_date = None

#Create a CSV reader object with a header
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        previous_profit = None

# Iterate through each row
        for row in reader:
            date = row['Date']
            profit = int(row['Profit/Losses'])

# Calculate increase and update maximum if needed
            if previous_profit is not None:
                increase = profit - previous_profit

                if increase > max_increase:
                    max_increase = increase
                    max_increase_date = date

            previous_profit = profit

    return max_increase_date, max_increase

#Call the greatest_profit_increase function and print the results
csv_file_path = csvpath
max_increase_date, max_increase = greatest_profit_increase(csvpath)

print(f'Greatest Increase in Profits:')
print(f'Date: {max_increase_date}')
print(f'Amount: ${max_increase}')

#Define a function to find the greatest profit decrease
def greatest_profit_decrease(csv_file_path):
    min_decrease = float('inf')
    min_decrease_date = None

    with open(csv_file_path, 'r') as csvfile:
        # Create a CSV reader object with a header 
        reader = csv.DictReader(csvfile)
        previous_profit = None


        # Iterate through each row
        for row in reader:
            date = row['Date']
            profit = int(row['Profit/Losses'])

            # Calculate decrease and update minimum if needed
            if previous_profit is not None:
                decrease = profit - previous_profit

                if decrease < min_decrease:
                    min_decrease = decrease
                    min_decrease_date = date

            previous_profit = profit

    return min_decrease_date, min_decrease

#Call the greatest_profit_decrease function and print the results
csv_file_path = csvpath
min_decrease_date, min_decrease = greatest_profit_decrease(csv_file_path)

print(f'Greatest Decrease in Profits:')
print(f'Date: {min_decrease_date}')
print(f'Amount: ${min_decrease}')

# Print analysis to terminal
print(f'Total Months: {total_months}')
print(f'Total Profit/Losses: ${total_profit_losses}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits:')
print(f'Date: {max_increase_date}')
print(f'Amount: ${max_increase}')
print(f'Greatest Decrease in Profits:')
print(f'Date: {min_decrease_date}')
print(f'Amount: ${min_decrease}')

    # Export results to text file
def analyze_profit_data(total_months, total_profit_losses, average_change, max_increase_date, max_increase, min_decrease_date, min_decrease):
    with open('budget_data_results.txt', 'w') as result_file:
        result_file.write(f'Total Months: {total_months}\n')
        result_file.write(f'Total Profit/Losses: ${total_profit_losses}\n')
        result_file.write(f'Average Change: ${average_change:.2f}\n')
        result_file.write(f'Greatest Increase in Profits:\n')
        result_file.write(f'Date: {max_increase_date}\n')
        result_file.write(f'Amount: ${max_increase}\n')
        result_file.write(f'Greatest Decrease in Profits:\n')
        result_file.write(f'Date: {min_decrease_date}\n')
        result_file.write(f'Amount: ${min_decrease}\n')

csv_file_path = csvpath
analyze_profit_data(total_months, total_profit_losses, average_change, max_increase_date, max_increase, min_decrease_date, min_decrease)