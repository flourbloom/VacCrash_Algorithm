def caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # shift letter, wrap around
            result += chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

print(caesar("Hello, World!", 3))  # Khoor, Zruog!
print(caesar(caesar("Hello, World!", 3),-3))  # Hello, World!

# Decrypt function
def decrypt_caesar(text,shift):
  return caesar(text, -shift)

print(decrypt_caesar("Khoor, Zruog!", 3))