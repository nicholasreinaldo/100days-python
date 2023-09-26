alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from cipher_art import logo
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def cipher(input_text, shift_amount, choice):
    letters = ""
    if choice == "encode":
        for char in range(0, len(input_text)):
            if input_text[char] not in alphabet:
                letters += str(input_text[char])
            else:
                letter_index = alphabet.index(input_text[char])
                position = letter_index + shift_amount
                if position > (len(alphabet)-1):
                    encoded_letter = alphabet[position % len(alphabet)]
                else:
                    encoded_letter = alphabet[position]
                letters += encoded_letter
        print(f"The encoded text is {letters}")
    elif choice == "decode":
        for char in range(0, len(input_text)):
            if input_text[char] not in alphabet:
                letters += str(input_text[char])
            else:
                letter_index = alphabet.index(input_text[char])
                position = letter_index - shift_amount
                if position < 0:
                    encoded_letter = alphabet[position % len(alphabet)]
                else:
                    encoded_letter = alphabet[position]
                letters += encoded_letter
        print(f"The encoded text is {letters}")

cipher(input_text=text, shift_amount=shift, choice=direction)

restart = input("Do you want to restart the program? \nType 'yes' if you want to go again. Otherwise type 'no'\n")
if restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher(input_text=text, shift_amount=shift, choice=direction)
elif restart == "no":
    print("Good bye")