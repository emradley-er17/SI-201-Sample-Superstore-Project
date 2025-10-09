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

# Download latest version
path = kagglehub.dataset_download("bravehart101/sample-supermarket-dataset")

print("Path to dataset files:", path)

