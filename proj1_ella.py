#Project 1 Checkpoint
# Name: Ella Kim
# Student ID: 28700423
# School Email: hayunkim@umich.edu
# Collaborators: Emma Radely
# USe of AI:
# Name of the Dataset: Sample Superstore Dataset
# Columns: Ship Mode, Segment, Region, Category, Profit, Sales, Quantity, State, Sub-Category
# Calculations:
    # 1. What is the average profit of all consumer goods in the East region? - Ella
    # 2. What percentage of Office Supplies that were shipped by First Class - Emma
    # 3. What percentage of Phones(sub-category) sold in California has a higher sales than 300? - Ella
    # 4. What is the average quanitity in each region? - Emma
import kagglehub
import csv

# Download latest version
path = kagglehub.dataset_download("bravehart101/sample-supermarket-dataset")


#  Q3. What percentage of Phones(sub-category) sold in California has a higher sales than 300? - Ella

def load_data(csv_file):
    records = []
    with open(csv_file, newline = '') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
        return records


def to_float(text):
    text = (text or "").replace(",", "").strip()
    return float(text) if text else 0.0


# GROUPING / FILTERING FUNCTIONS

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


# state_records: lists of 
def filter_subcatetory(state_records, subcategory):
    phone_records = []
    for r in state_records:
        if r.get("Sub-Category", "").strip().lower() == subcategory.strip().lower():
            phone_records.append(r)
    return phone_records


# Q1: Average profit of all Consumer goods in the East region
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


# Generate reports
def report_1(avg_profit):
    print(f"Q1) Average profit of all Consumer goods in the East region: {avg_profit:.2f}")

def report_3(percentage):
    print(f"Q3) Percentage of Phones in California with Sales > 300: {percentage:.2f}%")



def main():
    csv_file = "SampleSuperstore.csv"
    records = load_data(csv_file)

    
    califoria_records = group_by_states(records)
    avg_profit = avg_profit_consumer_east(records)
    report_1(avg_profit)

    phone_records = filter_subcatetory(califoria_records, "Phones")
    pct = percentage_high_sales(phone_records, 300)
    report_3(pct)

if __name__ == "__main__":
    main()
