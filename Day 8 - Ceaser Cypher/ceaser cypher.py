def encrypt(text, shift):
	result = []
	shift = shift % 26

	for char in text:
		if char.isalnum():
			base = ord('A') if char.isupper() else ord('a')
			result.append(chr((ord(char) - base + shift) % 26 + base))
		else:
			result.append(char)

	return ''.join(result)


def decrypt(text, shift):
	result = []
	shift = shift % 26

	for char in text:
		if char.isalnum():
			base = ord('A') if char.isupper() else ord('a')
			result.append(chr((ord(char) - base - shift) % 26 + base))
		else:
			result.append(char)

	return ''.join(result)

print("Welcome to the Caesar Cipher")
while True:
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? (E/D): ").strip().upper()
    if choice in ['E', 'D']:
        break
    else:
        print("Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")

text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))
if choice == 'E':
    result = encrypt(text, shift)
    print(f"Encrypted text: {result}")
else:
    result = decrypt(text, shift)
    print(f"Decrypted text: {result}")