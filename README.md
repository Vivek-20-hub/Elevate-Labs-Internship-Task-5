# Elevate-Labs-Internship-Task-5

## Exploratory Data Analysis (EDA) on cleaned_sales_data.csv
# Dataset Information:
-- Source: Kaggle (sales_data.csv)

-- Data Cleaning & Preprocessing: Data-Analyst-Internship-at-ElevateLabs-Task-

-- Cleaned Dataset: cleaned_sales_data.csv

Objectives:
Perform EDA using Pandas, Seaborn, and Matplotlib to extract trends, patterns, and insights.

Steps:
Import Required Modules

Load Pandas, Seaborn, and Matplotlib for data manipulation and visualization.

Load the Dataset

Import cleaned_sales_data.csv for analysis.

Perform Data Cleaning (if needed)

Handle missing values, duplicate entries, and outlier treatment.

Data Visualization

Use various graphs to explore and understand the dataset.

Visualizations & Insights:
1. Pairplot (Sample size: 1000)
Displays relationships between numerical variables.

Insights:

Concentrated clusters in postal codes show higher order placements from specific regions.

Few instances of high-cost products with low sales; low-cost products have larger sales volume.

More purchases are made for smaller quantities rather than bulk orders.

2. Heatmap
Reveals correlations between numerical features.

Insights:

Negative correlation between cost and profit: As cost increases, profit decreases.

Positive correlation between price and profit: Higher prices yield greater profit.

Positive correlation between quantity and sales: Higher quantity increases total sales.

3. Histogram
Shows distribution of sales data.

Insights:

Frequent low sales values suggest that smaller transactions dominate over large purchases.

4. Boxplot
Highlights distribution and outliers for sales across regions.

Insights:

75% of sales across all regions fall in the lower range.

Presence of a few extreme high-value sales transactions acting as outliers.

5. Scatterplot
Displays relationships between cost and profit.

Insights:

Strong negative correlation: Increasing cost leads to decreasing profit.

Sales patterns show clustering in specific price ranges.

Conclusion:
The dataset reveals clear trends: lower-cost products drive higher sales, and regional concentration impacts order volume. Cost directly affects profit, and transaction sizes remain predominantly small.
