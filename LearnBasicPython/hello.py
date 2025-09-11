# Ask User for name 
# Strip whitespace and capitalize the first letter of the name
# Combine from from 7 to 11
name = input("What is your name?").strip().title()


# # Remove whitespace from the string    
# name = name.strip()

# # Capitalize the first letter of the name
# name = name.title()



# Greet the user using comma
print("hello,", name)

# Greet the user using concatenation 
# notice no space after comma because it's connect with string
print("hello," + name)

# Greet the user using f-string
print(f"hello, {name}")

# Greet the user with just first name
first, last = name.split()
print (f"hello, {first}")





"""
This is a comment block
"""