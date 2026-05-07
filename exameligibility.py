# Program to check exam eligibility

# Taking input from the user
name = input("Enter your name: ")
attendance = float(input("Enter your attendance percentage: "))

# Checking eligibility
if attendance >= 75:
    print("\nHello", name)
    print("Your attendance is", attendance, "%")
    print("You are eligible to appear in the exam.")
else:
    print("\nHello", name)
    print("Your attendance is", attendance, "%")
    print("Sorry! You are not eligible to appear in the exam.")
    print("You need at least 75% attendance.")