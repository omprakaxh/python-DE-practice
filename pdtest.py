import pandas as pd

df = pd.read_csv("employees.csv")
"""
print(df)          # Print entire table
print(df.shape)    # (rows, columns)
print(df.columns)  # Column names
print(df.dtypes)   # Data types of each column
print(df.head(3))  # First 3 rows
print(df.tail(2)) 



print(df[df["Salary"] > 50000])

print("-" * 20)

print(df[df["Age"] > 30])

print("-" * 20)

print(df[df["City"] == "Mumbai"])


# Mini challenge - 1

print(df[(df["Salary"] > 50000) & (df["Age"] < 30)])


#print(df[(df["City"] == "Mumbai") | (df["City"] == "Delhi")])

print(df[df["City"].isin(["Mumbai", "Chennai", "Delhi"])])



# Sort Values:

sorted_df = df.sort_values("Salary",ascending = False)
#print(sorted_df)

# Average

average = df['Salary'].mean()
#print(average)

# MAX MIN SUM

max_salary = df['Salary'].max()
min_salary = df['Salary'].min()
total_salary = df['Salary'].sum()

#print(f"{max_salary} {min_salary} {total_salary}")

print(df['Salary'].describe())

"""

df["Tax"] = (df['Salary'] / 10 )
print(df)

df.to_csv('employees_updates.csv',index = False)