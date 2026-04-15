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




