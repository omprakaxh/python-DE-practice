"""

# Reading file from an txt.

print("\n The Method 1")

# Method 1 reading the whole file
with open("story.txt", "r") as file:
    content = file.read()

print(content)

print("\n The Method 2")

# Method 2 reading line by line
with open("story.txt","r") as file:
    for line in file:
        print(line.strip())

# Method 3 read all lines into a list

print("\n Method 3")

with open("story.txt","r") as file:
    lines = file.readlines()
print(lines) 



# Mini challenge - 1

with open("story.txt","r") as file:
    lines =  file.readlines()

for line in lines:
    if "Alice" in line:
        print(line.strip())


# Mini challenge 2

with open("story.txt","r") as f:
    lines = f.readlines()
index = 1
for line in lines:
    print(f"{index}. {line.strip()}")
    index+=1



# Mini challenge 3 - count total words

with open("story.txt","r") as f:
    lines = f.readlines()
count = 0
for line in lines:
    word = line.split()
    count += len(word)
print(count)

"""

# Mini challenge 4  - write a python file

with open("story.txt","r") as f:
    lines = f.readlines()

with open("output.txt","w") as out:
    for line in lines:
        word = line.split()
        if len(word) > 5:
            out.write(line)

        

