# Demonstrate different uses of split()

# Get user input
full_name = input("Enter your full name (with spaces): ")

# Using split() without arguments
print("\nUsing split() without arguments:")
print(full_name.split())  # Splits by any whitespace and removes empty strings

# Using split(" ") with space argument
print("\nUsing split(' ') with space argument:")
print(full_name.split(" "))  # Splits by exactly one space

# Example with multiple spaces
test_string = "John   Doe    Smith"
print("\nWith multiple spaces:")
print("Original string:", test_string)
print("Using split():", test_string.split())
print("Using split(' '):", test_string.split(" "))
