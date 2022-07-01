#Denine Harris
#gpa
# My app should ask for student name not allowing last name starting zzz ask
#gpa process GPA to list is student entry made deans list
last_name = input("Enter student's last name: ")

while last_name != 'ZZZ':
    first_name = input("Enter student's first name: ")

    gpa = float(input ("Enter student's gpa"))
    if gpa >= 3.5:
        print("Dean's list")

    if gpa > 3.25:
        print('Honor Roll')

    last_name = input("Enter student's last name: ")