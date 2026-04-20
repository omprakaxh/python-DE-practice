import datetime
journal = []  # list of dicts, one per entry

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
        diary.write(f"[{date}]\n")
        diary.write(f"{entry}\n")
        diary.write("-" * 20 + "\n")
        diary.write

def read_entry():
    with open("diary.txt", "r") as f:
        content = f.read()

    entries = content.split("-" * 20)

    for entry in entries:
        lines = entry.strip().split("\n")
        
        if lines[0] == "":  # skip empty chunks at end of file
            continue
        
        date = lines[0].strip("[]")
        text = "\n".join(lines[1:])

        journal.append({"date": date, "entry": text})  # ✅ add each entry as dict

    for item in journal:
        print(f"📅 {item['date']}")
        print(f"{item['entry']}")
        print("-" * 20)

def search_entry():
    keyword = input("Enter the keyword you want to search: ")

    for item in journal:
        if keyword in item["entry"]:
            print(f"📅 {item['date']}")
            print(f"{item['entry']}")
            print("-" * 20)

while True:
    print("1. Write entry📝")
    print("2. Read entry📖")
    print("3. Search entry🔍")
    print("4. Exit❌")

    choice = input("Choose an opetion 1-4: ")

    if choice == "1":
        write_entry()
    elif choice == "2":
        read_entry()
    elif choice == "3":
        search_entry()
    elif choice == "4":
        print("goodbye👋")
        break
    else:
        print("Invalid choice‼️")
        break
