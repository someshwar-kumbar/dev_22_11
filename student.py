import sys

if len(sys.argv) != 3:
    print("usage : python student.py <name> <rollno>")
    sys.exit(1)

script_name = sys.argv[0]
name = sys.argv[1]
rollno = sys.argv[2]   # corrected typo: sys.arge → sys.argv

print("script name :", script_name)
print("student name :", name)
print("roll number :", rollno)
