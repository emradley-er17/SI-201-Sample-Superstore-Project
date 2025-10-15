#Project 1 Checkpoint
# Name: Emma Radley
# Student ID: 8734 4694
# School Email: emradley@umich.edu
# Collaborators: Ella Kim
# Use of AI:
# Name of the Dataset: Sample Superstore Dataset
# Columns: Segment, Ship Mode, Region, Category, Profit, Sales, Quantity, State, Sub-Category
# Calculations:
    # 1. What is the average profit of all consumer goods in the East region? - Ella
    # 2. What percentage of Office Supplies that were shipped by First Class in the West region? - Emma
    # 3. What percentage of Phones(sub-category) sold in California has a higher sales than 300? - Ella
    # 4. What is the average quanitity and profit in each region? - Emma

import kagglehub
import os
import csv

# Download latest version of the dataset with Kagglehub
path = kagglehub.dataset_download("bravehart101/sample-supermarket-dataset")
print("Path to dataset files:", path)

#The path to CSV file
csv_file = os.path.join(path, "SampleSuperstore.csv")


#This Reads CSV and returns a list of dictionaries"
def load_data(csv_file):    
    data = []
    with open(csv_file, mode = 'r', newline='', encoding = 'utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# QUESTION 2: What percentage of Office Supplies that were shipped by First Class - Emma

#This function filters for rows where the "Category" is "Office Supplies"
def filter_data(data, conditions):
    """
    conditions: dict of {column: value}
    """
    return [row for row in data if all(row.get(k) == v for k, v in conditions.items())]

#This function counts how many of the rows that were office supplies were also shipped by "First Class" for "Ship Mode"
def count_first_class(filtered_data): 
    return sum(1 for row in filtered_data if row.get('Ship Mode') == 'First Class')     #For every matching row, it produces the number 1 and creates a sequence, adds up all the ones, and the total is the number of rows that sastifies the "First Class" condition.


def calculate_percentage(part,whole):
    if whole == 0:
        return 0.0
    return (part / whole) * 100

#This function prints out what the percentage of office supplies shipped by first class are and ensures that the percentage is a float value rounded to the nearest 2 decimal places.
def generate_report(percentage):
    print(f"Percentage of Office Supplies shipped by First Class in the West region: {percentage: .2f}%")

# QUESTION 4: What is the average quanitity of corporate goods in each region? - Emma
def average_corporate_quantity_by_region(data):
    region_totals = {}
    for row in data: 
        if row.get('Segment') == 'Corporate':  # Only consider Corporate segment
            region = row.get('Region')
            if region:
                quantity = int(row.get('Quantity', 0))
                if region not in region_totals:
                    region_totals[region] = {'total': 0, 'count': 0}
                region_totals[region]['total'] += quantity
                region_totals[region]['count'] += 1
   
   # Calculate the average per region
    averages = {}
    for region, values in region_totals.items():
        count = values['count']
        averages[region] = (values['total'] / count) if count else 0.0
    return averages


def main():
    data = load_data(csv_file)
    filtered_data = filter_data(data, {"Category": "Office Supplies", "Region": "West"})
    first_class_count = count_first_class(filtered_data)
    total_office_supplies_west = len(filtered_data)
    percentage = calculate_percentage(first_class_count, total_office_supplies_west)
    generate_report(percentage)

    averages = average_corporate_quantity_by_region(data)
    print("Average quantity of Corporate goods in each region:")
    for region, avg in averages.items():
        print(f"{region}: {avg:.2f}")

    #Loads the entire CSV file, Filters rows to just office supplies, counts office supplies shipped by first class, finds total number of office supply rows, calculates the percentage, prints the final result to the user. 

if __name__ == "__main__":
    main()


