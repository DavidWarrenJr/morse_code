def reverse_morse_code_dict():
    reversed_dict = {}
    for (key, value) in MORSE_CODE_DICT.items():
        reversed_dict[value] = key
    return reversed_dict


MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}
REVERSED_MORSE_CODE_DICT = reverse_morse_code_dict()


def encrypt(message):
    cipher = ""
    for letter in message:
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter.upper()] + " "
        else:
            cipher += " "

    return cipher


def decrypt(message):
    message += " "
    cipher_text = ""
    decoded_text = ""
    space_count = 0

    for letter in message:
        if letter != " ":
            space_count = 0
            cipher_text += letter
        # if space
        else:
            space_count += 1
            # check for new word
            if space_count == 2:
                decoded_text += " "
            else:
                decoded_text += REVERSED_MORSE_CODE_DICT[cipher_text]
                cipher_text = ""

    return decoded_text


def main():
    message = input("Enter a message to see it in morse code: ")

    encoded_message = encrypt(message)
    decoded_message = decrypt(encoded_message)

    print(encoded_message)
    print(decoded_message)


if __name__ == "__main__":
    main()
