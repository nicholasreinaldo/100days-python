alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from cipher_art import logo
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def cipher(input_text, shift_amount, choice):
    letters = ""
    if choice == "encode":
        for letter in range(0, len(input_text)):
            if input_text[letter] not in alphabet:
                letters += str(input_text[letter])
            else:
                letter_index = alphabet.index(input_text[letter])
                position = letter_index + shift_amount
                if position > (len(alphabet)-1):
                    encoded_letter = alphabet[position % len(alphabet)]
                else:
                    encoded_letter = alphabet[position]
                letters += encoded_letter
        print(f"The encoded text is {letters}")
    elif choice == "decode":
        for letter in range(0, len(input_text)):
            if input_text[letter] not in alphabet:
                letters += str(input_text[letter])
            else:
                letter_index = alphabet.index(input_text[letter])
                position = letter_index - shift_amount
                if position < 0:
                    encoded_letter = alphabet[position % len(alphabet)]
                else:
                    encoded_letter = alphabet[position]
                letters += encoded_letter
        print(f"The encoded text is {letters}")

cipher(input_text=text, shift_amount=shift, choice=direction)

restart = int(input("Do you want to restart the program? \nType 'yes' if you want to go again. Otherwise type 'no'\n"))
while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher(input_text=text, shift_amount=shift, choice=direction)

# def encrypt(plain_text, shift_amount):
#     letters = ""
#     for letter in range(0, len(plain_text)):
#         if plain_text[letter] == " ":
#             letters += " "
#         else:
#             letter_index = alphabet.index(plain_text[letter])
#             position = letter_index + shift_amount
#             if position > (len(alphabet)-1):
#                 encoded_letter = alphabet[position - len(alphabet)]
#             else:
#                 encoded_letter = alphabet[position]
#             letters += encoded_letter
#     print(f"The encoded text is {letters}")

# def decrypt(chipered_text, shift_amount):
#     letters = ""
#     for letter in range(0, len(chipered_text)):
#         if chipered_text[letter] == " ":
#             letters += " "
#         else:
#             letter_index = alphabet.index(chipered_text[letter])
#             position = letter_index - shift_amount
#             if position < 0:
#                 encoded_letter = alphabet[position + len(alphabet)]
#             else:
#                 encoded_letter = alphabet[position]
#             letters += encoded_letter
#     print(f"The encoded text is {letters}")

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(chipered_text=text, shift_amount=shift)