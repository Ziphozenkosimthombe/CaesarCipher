alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encryption(plainText, shiftKey):
    # convert the plain text to the cipher text
    # accept the plain text only.
    # and give you the output of the cipher text
    cipherText = ''
    for char in plainText:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shiftKey) % 26
            cipherText += alphabet[new_position]
        else:
            cipherText += char
    print(f"The text after encryption: {cipherText}")


def decryption(cipherText, shiftKey):
    # convert the cipher text to the plain text
    # only accept the input of the cipher text.
    # and give you the output of the cipher text
    plainText = ''
    for char in cipherText:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shiftKey) % 26
            plainText += alphabet[new_position]
        else:
            plainText += char
    print(f"The text after decryption: {plainText}")


end_the_program = False
while not end_the_program:

    what_to_do = input("Type 'encrypt' for encryption OR type 'decrypt' for decryption:  ")
    text = input("Type your message:\n ").lower()
    shift = int(input("Enter the key:\n"))

    # condition to call encryption or decryption

    if what_to_do == 'encrypt':
        # encryption pass text and the key
        encryption(plainText=text, shiftKey=shift)
    elif what_to_do == 'decrypt':
        decryption(cipherText=text, shiftKey=shift)

    play_again = input("type 'yes' to continue or 'no' to exit")
    if play_again == 'no':
        end_the_program = True
        print('have a nice day')