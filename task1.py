#Using the Pandas library, load a CSV file and perform basic data analysis tasks, such as calculating the average of a selected column. Additionally, use Matplotlib to create visualizations, including bar charts, scatter plots, and heatmaps, to analyze the data. Provide insights and observations based on the analysis and visualizations.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------
# LOAD CSV FILE
# ----------------------------
 # Change to your file name

df = pd.read_csv("marksheet.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumns in Dataset:")
print(df.columns.tolist())

# ----------------------------
# SELECT COLUMN FOR AVERAGE
# ----------------------------
column_name = input("\nEnter column name to calculate average: ")

if column_name not in df.columns:
    print("❌ Column not found. Please check spelling.")
    exit()

# Convert column to numeric (if needed)
df[column_name] = pd.to_numeric(df[column_name], errors='coerce')

avg = df[column_name].mean()
print(f"\n✅ Average of {column_name} = {avg}")

# ----------------------------
# BAR CHART
# ----------------------------
plt.figure()
df[column_name].value_counts().plot(kind='bar')
plt.title(f"Bar Chart of {column_name}")
plt.xlabel(column_name)
plt.ylabel("Frequency")
plt.show()

# ----------------------------
# SCATTER PLOT
# ----------------------------
numeric_cols = df.select_dtypes(include=np.number).columns

if len(numeric_cols) >= 2:
    x_col = numeric_cols[0]
    y_col = numeric_cols[1]

    plt.figure()
    plt.scatter(df[x_col], df[y_col])
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"Scatter Plot: {x_col} vs {y_col}")
    plt.show()
else:
    print("Not enough numeric columns for scatter plot.")

# ----------------------------
# HEATMAP
# ----------------------------
corr = df.corr(numeric_only=True)

plt.figure()
plt.imshow(corr)
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.show()
