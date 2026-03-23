# Basic if
print("Basic if")
age = 17
if age >= 17:
    print("you are adult")
print()

# if-else
print("if-else")
score = 80
if score >= 75:
    print("you passed!")
else:
    print("you failed.")
print()

# if-elif-else
print("if-elif-else")
grade = 89
if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 50:
    print("Grade: D")
else:
    print("Grade: F")
print()

# Comparison Operators
print("Comparison Operators")
x = 10
y = 20
print(f"x = {x}, y = {y}")
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)
print()

# Logical Operators
print("Logical Operators")
is_student = True
has_id = True

if is_student and has_id:
    print("access granted")
temperature = 32
if temperature < 0 or temperature > 40:
    print("extremes temperature!")
else:
    print("temperature is normal")
is_raining = False
if not is_raining:
    print("you can go outside")
print()

# Ternary
print("Ternary")
number = 12
result = "ganjil" if number % 2 != 0 else "genap"
print(f"{number} is {result}")