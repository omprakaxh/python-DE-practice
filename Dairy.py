import datetime

def write_entry():

    date = datetime.date.today()
    print("Write your entry (type 'DONE' on a new line when finished):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "DONE":  # Stop when user types DONE
            break
        lines.append(line)
    
    entry = "\n".join(lines)

    with open("diary.txt","a") as diary:
        diary.write(f"{date}\n")
        diary.write("\n")
        diary.write(f"{entry}\n")
        diary.write("\n")
        diary.write("-" * 20 + "\n")
while True:
    print("1. Write entry")
    print("2. Read entry")
    print("3. Search entry")
    print("4. Exit")

    choice = input("Choose an opetion 1-4: ")

    if choice == "1":
        write_entry()
    elif choice == "2":
        print("Read entry")
    elif choice == "3":
        print("Search entry")
    elif choice == "4":
        print("goodbye")
        break
    else:
        print("Invalid choice")
        break
