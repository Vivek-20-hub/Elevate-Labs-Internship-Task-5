# Elevate-Labs-Internship-Task-5

## Exploratory Data Analysis (EDA) on cleaned_sales_data.csv
---

# Dataset Information:
- Source: Kaggle (sales_data.csv)

- Data Cleaning & Preprocessing: Data-Analyst-Internship-at-ElevateLabs-Task-5

- Cleaned Dataset: cleaned_sales_data.csv
---
---
## Objectives:
Perform EDA using Pandas, Seaborn, and Matplotlib to extract trends, patterns, and insights.
---
---
## Steps:
- Import Required Modules

- Load Pandas, Seaborn, and Matplotlib for data manipulation and visualization.

- Load the Dataset

- Import cleaned_sales_data.csv for analysis.

- Perform Data Cleaning (if needed)

- Handle missing values, duplicate entries, and outlier treatment.

- Data Visualization

- Use various graphs to explore and understand the dataset.
---
## Visualizations & Insights:
---
## 1. Pairplot (Sample size: 1000) 
 **Displays relationships between numerical variables.**
![pairplot](https://github.com/user-attachments/assets/6815572c-e63d-402c-9e98-53c7a439f78f)

 # Insights:

- Concentrated clusters in postal codes show higher order placements from specific regions.

- Few instances of high-cost products with low sales; low-cost products have larger sales volume.

- More purchases are made for smaller quantities rather than bulk orders.
---

## 2. Heatmap
---
 **Reveals correlations between numerical features.**
 
![heatmap](https://github.com/user-attachments/assets/e38b77f3-62c9-4a84-bc99-fa33e0019f6e)

# Insights:

- Negative correlation between cost and profit: As cost increases, profit decreases.

- Positive correlation between price and profit: Higher prices yield greater profit.

- Positive correlation between quantity and sales: Higher quantity increases total sales.
---

## 3. Histogram
---

**Shows distribution of sales data.**

![sales_histogram](https://github.com/user-attachments/assets/328e70d8-8f09-4161-ab36-96966ca8810a)

# Insights:

- Frequent low sales values suggest that smaller transactions dominate over large purchases.
---

## 4. Boxplot
---
**Highlights distribution and outliers for sales across regions.**
![sales_region_boxplot](https://github.com/user-attachments/assets/016c2544-0e9b-4e07-8381-902fa1b28992)

# Insights:

- 75% of sales across all regions fall in the lower range.

- Presence of a few extreme high-value sales transactions acting as outliers.
---

## 5. Scatterplot
---
**Displays relationships between cost and profit.**

![profit_cost_scatterplot](https://github.com/user-attachments/assets/93583175-3db8-4938-9208-fa03cf76c782)

# Insights:

- Strong negative correlation: Increasing cost leads to decreasing profit.

- Sales patterns show clustering in specific price ranges.
---

## Conclusion:
---
- The dataset reveals clear trends: lower-cost products drive higher sales, and regional concentration impacts order volume. Cost directly affects profit, and transaction sizes remain predominantly small.
--- 
