from art import logo

print(logo)

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr(start + (ord(char) - start - shift) % 26)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def main_program():
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
        if direction not in ['encode', 'decode']:
            print("Invalid option. Please enter 'encode' or 'decode'.")
            continue
        
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        
        if direction == "decode":
            result = decrypt(text, shift)
            print(f"The decoded text is {result}")
        else:
            result = encrypt(text, shift)
            print(f"The encoded text is {result}")
        
        user_input = input("Do you want to continue? (continue/not): ").strip().lower()
        if user_input == "not":
            print("Ending the program.")
            break
        elif user_input != "continue":
            print("Invalid input. Ending the program.")
            break

main_program()
