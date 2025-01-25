from morse_code_logo import intro, exit
from morse_code_list_conversion import dict1
import time

def convert_to_morse_code():
    message = input("Enter the sentence: \n").upper()
    encoded_message = ''
    for letter in message:
        if letter in dict1:
            encoded_message = encoded_message + dict1[letter] + " "
        else:
            print(f"Invalid character '{letter}' in input. Skipping.")
    print(f"Encoded Morse Code: \n{encoded_message}\n")

def convert_from_morse_code():
    list1 = []
    decoded_code = ''
    code = input("Enter the message to be decoded:\n")
    list1 = code.split(" ")
    for i in list1:
        matched = False
        for keys in dict1:
            if i == dict1[keys]:
                decoded_code += keys
                matched = True
                break
        if not matched:
            print(f"Invalid Morse code '{i}' detected.")
            return
    print(f"Decoded Message: \n{decoded_code}\n")

def main():
    print(intro)
    still_continue = True
    while still_continue:
        choose = input("Enter whether you want to encode or decode the message, otherwise enter 'stop': ").lower()
        if choose == "encode":
            convert_to_morse_code()
        elif choose == "decode":
            convert_from_morse_code()
        elif choose == "stop":
            print(exit)
            time.sleep(3)
            still_continue = False
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
