#Project 1 Checkpoint
# Name: Ella Kim
# Student ID: 
# School Email:
# Collaborators: Emma
# USe of AI:
# Name of the Dataset: Sample Superstore Dataset
# Columns: Ship Mode, Region, Category, Profit, Sales, Quantity, State, Sub-Category
# Calculations:
    # 1. What is the average profit in the East region? - Ella
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

# records: list of dictionaries
# state: targeted state - California
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

def to_float(text):
    text = (text or "").replace(",", "").strip()
    return float(text) if text else 0.0

def calculate_percentage_high_sales(phone_records, threshold):
    total = 0
    count_over = 0
    for r in phone_records:
        sales_value = to_float(r.get("Sales", "0"))
        total += 1
        if sales_value > threshold:
            count_over += 1
    if total == 0:
        return 0.0
    return (count_over / total) * 100

def generate_report(percentage):
    print(f"Percentage of Phones in California with Sales > 300: {percentage:.2f}%")

def main():
    csv_file = "SampleSuperstore.csv"
    records = load_data(csv_file)

    califoria_records = group_by_states(records)

    phone_records = filter_subcatetory(califoria_records, "Phones")
    pct = calculate_percentage_high_sales(phone_records, 300)
    generate_report(pct)

if __name__ == "__main__":
    main()
