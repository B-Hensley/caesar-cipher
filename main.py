import string

ALPHABET = list(string.ascii_lowercase)
DIRECTIONS = ['encode', 'decode']
direction = ''

while direction not in DIRECTIONS:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction in DIRECTIONS:
        break

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ''
        
    for letter in original_text:
        
        if letter in ALPHABET:     
            if encode_or_decode == "encode":
                shifted_position = ALPHABET.index(letter) + shift_amount
                shifted_position %= len(ALPHABET)
                output_text += ALPHABET[shifted_position]
                
            elif encode_or_decode == "decode":
                shifted_position = ALPHABET.index(letter) - shift_amount
                shifted_position %= len(ALPHABET)
                output_text += ALPHABET[shifted_position]

            else: 
                print("Please enter 'encode' or 'decode'")
                
        else:
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")
    
    

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)