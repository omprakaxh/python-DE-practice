import csv
"""
print("Method 1: rows as List using reader function")
with open("employees.csv","r") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)

print("Method 1: rows as List using reader function")
with open("employees.csv","r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)

print("Method 3")

import csv

with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} lives in {row['City']}")


# Mini challenge - 1

with open("employees.csv","r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if int(row["Salary"]) > 50000:
            print(f"{row["Name"]} earns more than 50000")




#Mini challenge 2

new_row = ["Frank","27","Hyderabad","70000"]

with open("employees.csv","a",newline="") as f:
    file = csv.writer(f)
    file.writerow(new_row)

"""

# Mini challenge 3

with open("employees.csv","r") as f:
    content = csv.DictReader(f)

    with open("high_earning.csv","w",newline="") as p:
        file = csv.DictWriter(p, fieldnames = ["Name","Age","City","Salary"])
        file.writeheader()
        for row in content:
            if int(row["Salary"]) >= 55000:
                file.writerow(row)










