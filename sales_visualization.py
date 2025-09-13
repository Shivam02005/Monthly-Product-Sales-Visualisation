import pandas as pd
import matplotlib.pyplot as plt
import os

# --- 1. Load Data ---
# Load the dataset from the CSV file
try:
    df = pd.read_csv('data/monthly_sales_data.csv')
except FileNotFoundError:
    print("Error: 'data/monthly_sales_data.csv' not found.")
    print("Please make sure the CSV file is in the 'data' directory.")
    exit()

# --- 2. Data Preparation ---
# Ensure 'Month' is treated as a categorical variable in chronological order
month_order = ['January', 'February', 'March', 'April', 'May', 'June']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

# Create the output directory if it doesn't exist
output_dir = 'visualizations'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- 3. Generate Visualizations ---

# Visualization 1: Bar Chart - Total Sales by Product
print("Generating Bar Chart: Sales by Product...")
sales_by_product = df.groupby('Product')['Units Sold'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sales_by_product.plot(kind='bar', color='skyblue')
plt.title('Total Units Sold by Product', fontsize=16)
plt.xlabel('Product', fontsize=12)
plt.ylabel('Total Units Sold', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout() # Adjust layout to make room for labels
plt.savefig(os.path.join(output_dir, 'sales_by_product_bar_chart.png'))
print("Saved 'sales_by_product_bar_chart.png'")

# Visualization 2: Line Chart - Monthly Revenue Trend
print("Generating Line Chart: Monthly Revenue Trend...")
monthly_revenue = df.groupby('Month')['Revenue'].sum()

plt.figure(figsize=(10, 6))
monthly_revenue.plot(kind='line', marker='o', color='green', linestyle='-')
plt.title('Monthly Revenue Trend', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'monthly_revenue_trend_line_chart.png'))
print("Saved 'monthly_revenue_trend_line_chart.png'")


# Visualization 3: Pie Chart - Revenue Contribution by Category
print("Generating Pie Chart: Product Category Contribution...")
revenue_by_category = df.groupby('Category')['Revenue'].sum()

plt.figure(figsize=(8, 8))
plt.pie(revenue_by_category, labels=revenue_by_category.index, autopct='%1.1f%%',
        startangle=140, colors=['gold', 'lightcoral'])
plt.title('Revenue Contribution by Product Category', fontsize=16)
plt.ylabel('') # Hides the 'Revenue' label on the y-axis
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig(os.path.join(output_dir, 'category_contribution_pie_chart.png'))
print("Saved 'category_contribution_pie_chart.png'")


# Display the charts
print("\nDisplaying all charts...")
plt.show()
print("Done.")
