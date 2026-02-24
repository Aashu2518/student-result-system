students = []

def add_student():
    name = input("Name: ")
    marks = int(input("Marks: "))
    students.append([name, marks])
    with open("students.txt","a") as f:
        f.write(name+","+str(marks)+"\n")
    print("Student Added")

def view_students():
    try:
        with open("students.txt") as f:
            print(f.read())
    except:
        print("No data")

def search_student():
    key=input("Enter name: ")
    with open("students.txt") as f:
        for line in f:
            if key.lower() in line.lower():
                print(line)

def average():
    total=0
    count=0
    with open("students.txt") as f:
        for line in f:
            total+=int(line.split(",")[1])
            count+=1
    print("Average:",total/count)

while True:
    print("\n1.Add 2.View 3.Search 4.Average 5.Exit")
    c=input()

    if c=="1":
        add_student()
    elif c=="2":
        view_students()
    elif c=="3":
        search_student()
    elif c=="4":
        average()
    else:
        break
