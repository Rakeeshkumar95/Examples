import os
#Author: Rakeesh
#Student Database
student_db = {}
#no_of_students = 0
# Ask user on how many to be enrolled
no_of_students = int(input("Number of students to be enrolled:"))

for entry in range(0,no_of_students):
    id = input("Enter the student Id:")
    name = input("Enter the student name:")
    student_db[id] = name

while True:
    _ = os.system("cls")
    #Search the student
    choice = int(input("What do you want to do: \n Press 1: for full list. \n Press 2:for search. \n Press 3: Exit."))
    if choice == 1:
        for entry in student_db.keys():
            print(f"{entry} : {student_db[entry]}")
    elif choice == 2:
        print("You are searching now.")
        search_id = input("Enter the student Id:")
        print(f"Student name of id {search_id} is {student_db[search_id]}")
    elif choice == 3:
        print("Thanks for using my app. Now Exiting the app")
        break
    else:
        print("WRONG REQUEST. PLEASE CHECK THE ENTRY. IT MUST BE 1 or 2 or 3.. EXITING THE APP")
        break