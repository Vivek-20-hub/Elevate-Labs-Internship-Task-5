import pandas as pd
import matplotlib as mpl
import seaborn as sns

df = pd.read_csv("/content/cleaned_sales_data.csv")

df.dropna(how="any")
df.drop_duplicates()

print(df.describe(include="all"))
df.info()
print(df['segment'].value_counts())

sns.pairplot(df.sample(1000), hue="segment", diag_kind="kde")
mpl.pyplot.savefig("pairplot.png")
mpl.pyplot.clf()

tempdf = df.copy()
tempdf.drop(columns=["row_id", "order_id", "order_date", "ship_date", "ship_mode", "customer_name", "customer_id", "segment", "country", "city", "state", "postal_code", "region", "product_id", "category", "sub_category", "product_name"], inplace=True)
sns.heatmap(tempdf.corr(), annot=True, cmap="coolwarm")
mpl.pyplot.title("Correlation Heatmap")
mpl.pyplot.savefig("heatmap.png")
mpl.pyplot.clf()

sns.histplot(data=df, x="sales", bins=30, kde=True)
mpl.pyplot.title("Sales Distribution")
mpl.pyplot.xlabel("Sales Amount")
mpl.pyplot.ylabel("Frequency")
mpl.pyplot.savefig("sales_histogram.png")
mpl.pyplot.clf()

sns.boxplot(data=df, x="region", y="sales", hue="segment")
mpl.pyplot.xlabel("Region")
mpl.pyplot.ylabel("Sales")
mpl.pyplot.title("Sales by Region and Segment")
mpl.pyplot.legend(title="Segment")
mpl.pyplot.savefig("sales_region_boxplot.png")
mpl.pyplot.clf()

sns.scatterplot(data=df, x="profit", y="cost", hue="region", size="sales")
mpl.pyplot.title("Cost vs Profit by Region")
mpl.pyplot.savefig("profit_cost_scatterplot.png")
mpl.pyplot.clf()
