age = int(input("Enter your Age: "))
if age < 0:
    print("Invalid age!")
elif age <= 12:
    print("You are a CHILD")
elif age <= 19:
    print ("You are a TEEN")
elif age <= 64:
    print("You are an ADULT")
else:
    print("You are a SENIOR")