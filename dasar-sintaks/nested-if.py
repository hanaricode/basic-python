# Basic Nested if
print("Basic Nested if")
age = 20
has_license = True

if age >= 17:
    print("Old enough to drive")
    if has_license:
        print("you have a license — you cant drive!")
    else:
        print("but you don't have a license yet")
else:
    print("you are too young to drive")
print()

# Nested if-else
print("Nested if-else")
print("Login system")
username = "hanari"
password = "hanari123"

input_user = "hanari"
input_pass = "hanari123"

if input_user == username:
    if input_pass == password:
        print("login successful! Welcome,", username)
    else:
        print("wrong password.")
else:
    print("username not found.")
print()

# Multiple Conditions
print("Multiple Conditions")
print("Ticket price System")
age = 20
is_member = True

if age < 10:
    print("Child ticket: free")
else:
    if age >= 30:
        print("senior ticket: $8")
    else:
        if is_member:
            print("member ticket: $5")
        else:
            print("regular ticket: $10")
print()

# Nested if with logical operators
print("Nested if with logical operators")
print("Job Application")
gpa = 3.53
experience = 2
has_certificate = True

if gpa >= 3.0:
    if experience >= 1 or has_certificate:
        if experience >= 3:
            print("Accepted as Senior Developer")
        else:
            print("Accepted as Junior Developer")
    else:
        print("Need more experience or a certificate")
else:
    print("GPA does not meet the requirement")