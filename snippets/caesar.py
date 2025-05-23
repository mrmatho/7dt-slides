import sys

def caesar_cipher(text, shift):
    result = ""
    # Traverse the text
    for i in range(len(text)):
        char = text[i]
        if char == " ":
            result += char
        # Encrypt uppercase characters
        elif char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)

    return result

# Check if the script is run directly
if len(sys.argv) > 2:
    m = sys.argv[1:]
else:
    m = []
msg = " ".join(m)

print(msg)
for i in range(1, 26):
    print(f"Shift {i}: {caesar_cipher(msg, i)}")

