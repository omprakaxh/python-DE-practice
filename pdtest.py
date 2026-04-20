import pandas as pd

df = pd.read_csv("employees.csv")
"""
print(df)          # Print entire table
print(df.shape)    # (rows, columns)
print(df.columns)  # Column names
print(df.dtypes)   # Data types of each column
print(df.head(3))  # First 3 rows
print(df.tail(2)) 

"""

print(df[df["Salary"] > 50000])

print("-" * 20)

print(df[df["Age"] > 30])

print("-" * 20)

print(df[df["City"] == "Mumbai"])