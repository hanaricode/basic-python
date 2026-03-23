name = "Hanari"
age = 20
height = 1.69
score = 95.2117

# f-string
print("f-string")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height:.2f} m")
print(f"Score: {score:.2f}")
print()

# format() method
print("format() method")
print("Name: {}".format(name))
print("Age: {}".format(age))
print("Name and age: {} is {} years old".format(name, age))
print("With index: {0} is {1} years old, {0} loves Python".format(name, age))
print()

# % formatting
print("% formatting")
print("Name: %s" % name)
print("Age: %d" % age)
print("Height: %.2f" % height)
print()

# Alignment
print("Alignment")
print(f"{'Left':<15} |")
print(f"{'Center':^15} |")
print(f"{'Right':>15} |")
print()

# Number formatting
print("Number Formatting")
big_number = 1000000000
pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286

print(f"Thousand separator: {big_number:,}")
print(f"Pi (2 decimal): {pi:.2f}")
print(f"Pi (4 decimal): {pi:.4f}")
print(f"Percentage: {0.875:.1%}")
print(f"Binary: {10:b}")
print(f"Hexadecimal: {255:x}")