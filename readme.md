# Monthly Product Sales Visualization

## Project Overview

This project focuses on visualizing monthly product sales data using Python. The goal is to analyze sales patterns and revenue trends through various charts created with the Matplotlib library.

### Problem Statement
Visualize monthly product sales using different chart types in Matplotlib.

### Key Objectives
-   **Bar Chart**: Analyze total units sold for each product.
-   **Line Chart**: Track the revenue trend over several months.
-   **Pie Chart**: Understand the contribution of each product category to the total revenue.

---

## Repository Structure

The project is organized as follows:

```
.
├── data/
│   └── monthly_sales_data.csv   # Input dataset
├── visualizations/
│   └── ... (Generated chart images)
├── sales_visualization.py       # Main Python script for analysis and visualization
├── requirements.txt             # Required Python packages
└── README.md                    # Project documentation
```

---

## Setup and Installation

To run this project, you need Python 3 and the libraries listed in `requirements.txt`.

**1. Clone the repository:**
```bash
git clone <your-repository-url>
cd monthly-sales-visualization
```

**2. Create a virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

**3. Install the required packages:**
```bash
pip install -r requirements.txt
```

---

## How to Run the Project

Execute the main Python script from the root directory of the project:

```bash
python sales_visualization.py
```

The script will:
1.  Read the data from `data/monthly_sales_data.csv`.
2.  Generate the three specified charts.
3.  Save the charts as PNG files in the `visualizations/` directory.
4.  Display the charts on your screen.

---

## Output Visualizations

### 1. Bar Chart: Total Units Sold by Product
This chart shows the performance of individual products based on the number of units sold.

<img width="2400" height="1600" alt="image" src="https://github.com/user-attachments/assets/34a599eb-18d0-43b9-9115-44c41d0ab146" />


### 2. Line Chart: Monthly Revenue Trend
This chart illustrates the flow of total revenue over the months, helping to identify seasonal trends or growth.

<img width="2400" height="1600" alt="image (1)" src="https://github.com/user-attachments/assets/068e74f2-fae3-4f35-97b7-39a629f8af4e" />


### 3. Pie Chart: Revenue by Category
This chart breaks down the total revenue by product category, showing which categories are most valuable.

<img width="2400" height="1600" alt="image (2)" src="https://github.com/user-attachments/assets/98e23a72-ba9b-4b90-b492-fdfabb81599c" />
