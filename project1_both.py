import kagglehub
import os
import csv

# Download latest version
path = kagglehub.dataset_download("bravehart101/sample-supermarket-dataset")

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

# Q1: Average profit of all Consumer goods in the East region -Ella
def calculate_average_profit(region_result, segment_results):
    total = 0.0
    count = 0
    for r in segment_results:
        profit_value = to_float(r.get("Profit", "0"))
        total += profit_value
        count += 1
    if count == 0:
        return 0.0
    return total / count

def avg_profit_consumer_east(records):
    region_result = group_by_region(records, "East")
    segment_results = group_by_segment(region_result, "Consumer")
    avg_profit = calculate_average_profit(region_result, segment_results)
    return avg_profit

def percentage_high_sales(phone_records, threshold):
    total = 0
    count_over = 0
    for r in phone_records:
        sales_value = to_float(r.get("Sales", "0"))
        total += 1
        if sales_value > threshold:
            count_over += 1
    if total == 0:
        return 0.0
    return (count_over / total) * 100.0

# File output for Q1 as txt
def write_avg_profit_to_txt(avg_profit, filename="q1_output.txt"):
    with open(filename, "w") as f:
        f.write(f"Q1) Average profit of all Consumer goods in the East region: {avg_profit:.2f}\n")


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

# file output function for Q2
def write_percentage_to_txt(percentage, filename="q2_percentage_output.txt"):
    """
    Writes the Q2 result to a TXT file.
    """
    with open(filename, "w") as file:
        file.write("Question 2: What percentage of Office Supplies were shipped by First Class in the West region?\n")
        file.write(f"Answer: {percentage:.2f}%\n")

#This function prints out what the percentage of office supplies shipped by first class are and ensures that the percentage is a float value rounded to the nearest 2 decimal places.
def generate_report(percentage):
    print(f"Q2) Percentage of Office Supplies shipped by First Class in the West region: {percentage: .2f}%")

#  Q3. What percentage of Phones(sub-category) sold in California has a higher sales than 300? - Ella

def to_float(text):
    text = (text or "").replace(",", "").strip()
    return float(text) if text else 0.0

# file output for Q3 as txt
def write_pct_high_sales_to_txt(pct, filename="q3_output.txt"):
    with open(filename, "w") as f:
        f.write("Q3) Percentage of Phones in California with Sales > 300:\n")
        f.write(f"{pct:.2f}%\n")

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

# file output for Q4:
def write_average_corporate_quantity_to_txt(averages, filename="q4_output.txt"):
    with open(filename, "w") as f:
        f.write("Q4) Average quantity of Corporate goods in each region:\n")
        for region, avg in averages.items():
            f.write(f"{region}: {avg:.2f}\n")

# GROUPING / FILTERING FUNCTIONS -Ella 

# records: list of dictionaries
# state: targeted state - California
def group_by_region(records, region):
    result = []
    target = region.strip().lower()
    for r in records:
        if r.get("Region", "").strip().lower() == target:
            result.append(r)
    return result


def group_by_segment(records, segment):
    result = []
    target = segment.strip().lower()
    for r in records:
        if r.get("Segment", "").strip().lower() == target:
            result.append(r)
    return result


def group_by_states(records):
    result = []

    for r in records:
        state_value = r.get("State", "").strip().lower()
        if state_value == "california":
            result.append(r)
    return result


# state_records: lists of -Ella
def filter_subcategory(state_records, subcategory):
    phone_records = []
    for r in state_records:
        if r.get("Sub-Category", "").strip().lower() == subcategory.strip().lower():
            phone_records.append(r)
    return phone_records


# Generate reports -Ella
def report_1(avg_profit):
    print(f"Q1) Average profit of all Consumer goods in the East region: {avg_profit:.2f}")

def report_3(percentage):
    print(f"Q3) Percentage of Phones in California with Sales > 300: {percentage:.2f}%")

# START OF TEST CASES: 
def test_percentage_office_supplies_first_class_west(): # Q2: -Emma
    # General Test Case 1: Some first class, some not
    data1 = [
        {'Category': 'Office Supplies', 'Region': 'West', 'Ship Mode': 'First Class'},
        {'Category': 'Office Supplies', 'Region': 'West', 'Ship Mode': 'Second Class'},
        {'Category': 'Office Supplies', 'Region': 'West', 'Ship Mode': 'First Class'},
        {'Category': 'Furniture', 'Region': 'West', 'Ship Mode': 'First Class'},
        {'Category': 'Office Supplies', 'Region': 'East', 'Ship Mode': 'First Class'},
    ]
    filtered = filter_data(data1, {"Category": "Office Supplies", "Region": "West"})
    count = count_first_class(filtered)
    total = len(filtered)
    expected = (2/3) * 100
    result = calculate_percentage(count, total)
    assert abs(result - expected) < 0.001, f"General Test 1 failed: got {result}, expected {expected}"

    # General Test Case 2: All Office Supplies are First Class
    data2 = [
        {'Category': 'Office Supplies', 'Region': 'West', 'Ship Mode': 'First Class'},
        {'Category': 'Office Supplies', 'Region': 'West', 'Ship Mode': 'First Class'},
    ]
    filtered = filter_data(data2, {"Category": "Office Supplies", "Region": "West"})
    count = count_first_class(filtered)
    total = len(filtered)
    expected = 100.0
    result = calculate_percentage(count, total)
    assert abs(result - expected) < 0.001, f"General Test 2 failed: got {result}, expected {expected}"

    # Edge Case 1: No matching office supplies in the West
    data3 = [
        {'Category': 'Furniture', 'Region': 'West', 'Ship Mode': 'First Class'},
        {'Category': 'Office Supplies', 'Region': 'East', 'Ship Mode': 'First Class'},
    ]
    filtered = filter_data(data3, {"Category": "Office Supplies", "Region": "West"})
    count = count_first_class(filtered)
    total = len(filtered)
    expected = 0.0
    result = calculate_percentage(count, total)
    assert abs(result - expected) < 0.001, f"Edge Test 1 failed: got {result}, expected {expected}"

    # Edge Case 2: Empty data
    data4 = []
    filtered = filter_data(data4, {"Category": "Office Supplies", "Region": "West"})
    count = count_first_class(filtered)
    total = len(filtered)
    expected = 0.0
    result = calculate_percentage(count, total)
    assert abs(result - expected) < 0.001, f"Edge Test 2 failed: got {result}, expected {expected}"

    print("All tests for percentage_office_supplies_first_class_west passed!")

    
def test_average_corporate_quantity_by_region(): #Q4: -Emma
    # General Test Case 1: Multiple regions with corporate orders
    data1 = [
        {'Segment': 'Corporate', 'Region': 'West', 'Quantity': '5'},
        {'Segment': 'Corporate', 'Region': 'West', 'Quantity': '3'},
        {'Segment': 'Corporate', 'Region': 'East', 'Quantity': '7'},
        {'Segment': 'Corporate', 'Region': 'East', 'Quantity': '9'},
        {'Segment': 'Consumer', 'Region': 'West', 'Quantity': '100'},
    ]
    expected1 = {'West': 4.0, 'East': 8.0}
    result1 = average_corporate_quantity_by_region(data1)
    assert result1 == expected1, f"General Test 1 failed: got {result1}, expected {expected1}"

    # General Test Case 2: Only one corporate region
    data2 = [
        {'Segment': 'Corporate', 'Region': 'West', 'Quantity': '10'},
        {'Segment': 'Consumer', 'Region': 'East', 'Quantity': '10'},
    ]
    expected2 = {'West': 10.0}
    result2 = average_corporate_quantity_by_region(data2)
    assert result2 == expected2, f"General Test 2 failed: got {result2}, expected {expected2}"

    # Edge Case 1: No corporate entries
    data3 = [
        {'Segment': 'Consumer', 'Region': 'West', 'Quantity': '5'},
    ]
    expected3 = {}
    result3 = average_corporate_quantity_by_region(data3)
    assert result3 == expected3, f"Edge Test 1 failed: got {result3}, expected {expected3}"

    # Edge Case 2: Corporate entries with all zero quantities
    data4 = [
        {'Segment': 'Corporate', 'Region': 'Midwest', 'Quantity': '0'},
        {'Segment': 'Corporate', 'Region': 'Midwest', 'Quantity': '0'}
    ]
    expected4 = {'Midwest': 0.0}
    result4 = average_corporate_quantity_by_region(data4)
    assert result4 == expected4, f"Edge Test 2 failed: got {result4}, expected {expected4}"

    print("All tests for average_corporate_quantity_by_region passed!")

def main(): # -Both
    csv_file = "SampleSuperstore.csv"
    records = load_data(csv_file)

    
    california_records = group_by_states(records)
    avg_profit = avg_profit_consumer_east(records)
    report_1(avg_profit)
    write_avg_profit_to_txt(avg_profit)

    phone_records = filter_subcategory(california_records, "Phones")
    pct = percentage_high_sales(phone_records, 300)
    report_3(pct)
    write_pct_high_sales_to_txt(pct)

    data = load_data(csv_file)
    filtered_data = filter_data(data, {"Category": "Office Supplies", "Region": "West"})
    first_class_count = count_first_class(filtered_data)
    total_office_supplies_west = len(filtered_data)
    percentage = calculate_percentage(first_class_count, total_office_supplies_west)
    generate_report(percentage)
    write_percentage_to_txt(percentage)


    averages = average_corporate_quantity_by_region(data)
    print("Q4) Average quantity of Corporate goods in each region:")
    for region, avg in averages.items():
        print(f"{region}: {avg:.2f}")
    write_average_corporate_quantity_to_txt(averages)

if __name__ == "__main__":
    test_percentage_office_supplies_first_class_west()
    test_average_corporate_quantity_by_region()
    main()
