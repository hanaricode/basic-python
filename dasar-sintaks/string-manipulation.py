text = "Hii. Welcome to my World!"

# Basic info
print("Original:", text)
print("Length:", len(text))
print()

# Case
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())
print("Swap case:", text.swapcase())
print()

# Slicing
print("First 5 chars:", text[:5])
print("Last 6 chars:", text[-6:])
print("Reverse:", text[::-1])
print()

# Search and check
print("Starts with 'Hello':", text.startswith("Hello"))
print("Ends with '!':", text.endswith("!"))
print("Find 'World':", text.find("World"))
print("Count 'l':", text.count("l"))
print()

# Modify
print("Replace:", text.replace("World", "Python"))
print("Strip spaces:", "  hello  ".strip())
print("Left strip:", "  hello  ".lstrip())
print("Right strip:", "  hello  ".rstrip())
print()

# Split and join
words = text.split(", ")
print("Split:", words)
print("Join:", " - ".join(words))