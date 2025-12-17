
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("sales_data.csv")

# Seaborn style
sns.set_theme(style="whitegrid")

# Box Plot
plt.figure()
sns.boxplot(x="Category", y="Price", data=df)
plt.title("Price Distribution by Category")
plt.show()

# Heatmap
plt.figure()
corr = df[["Sales", "Price", "Customers"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Plotly Line Chart
fig = px.line(df, x="Month", y="Sales", title="Monthly Sales Trend", markers=True)
fig.show()

# Plotly Bar Chart
fig2 = px.bar(df, x="Category", y="Sales", title="Sales by Category")
fig2.show()
