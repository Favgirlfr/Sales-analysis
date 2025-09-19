import pandas as pd
import matplotlib.pyplot as plt

# Load dataset from CSV
df = pd.read_csv("sales.csv")

# Preview data
print(df.head())

# Check structure
print(df.info())

# Check missing values
print(df.isnull().sum())

# Fill or drop missing values (if any)
df = df.dropna()
# Basic statistics
print(df.describe())

# Total sales revenue = Quantity * Price
df["Revenue"] = df["Quantity"] * df["Price"]

# Average revenue per product
print(df.groupby("Product")["Revenue"].mean())

df.groupby("Date")["Revenue"].sum().plot(kind="line", marker="o")
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.show()

df.groupby("Product")["Quantity"].sum().plot(kind="bar", color="skyblue")
plt.title("Total Quantity Sold per Product")
plt.xlabel("Product")
plt.ylabel("Total Quantity")
plt.show()

df["Price"].plot(kind="hist", bins=10, color="orange", alpha=0.7)
plt.title("Distribution of Product Prices")
plt.xlabel("Price")
plt.show()

plt.scatter(df["Quantity"], df["Revenue"], alpha=0.6, c="green")
plt.title("Quantity vs Revenue")
plt.xlabel("Quantity")
plt.ylabel("Revenue")
plt.show()

