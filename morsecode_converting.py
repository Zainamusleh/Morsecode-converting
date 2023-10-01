morse_code = {'A':'.-', 'B':'-...',
              'C':'-.-.', 'D':'-..', 'E':'.',
              'F':'..-.', 'G':'--.', 'H':'....',
              'I':'..', 'J':'.---', 'K':'-.-',
              'L':'.-..', 'M':'--', 'N':'-.',
              'O':'---', 'P':'.--.', 'Q':'--.-',
              'R':'.-.', 'S':'...', 'T':'-',
              'U':'..-', 'V':'...-', 'W':'.--',
              'X':'-..-', 'Y':'-.--', 'Z':'--..',
              '1':'.----', '2':'..---', '3':'...--',
              '4':'....-', '5':'.....', '6':'-....',
              '7':'--...', '8':'---..', '9':'----.',
              '0':'-----', ', ':'--..--', '.':'.-.-.-',
              '?':'..--..', '/':'-..-.', '-':'-....-',
              '(':'-.--.', ')':'-.--.-', ' ':' '
             }  

def morsecode_conversion(text):
    morse = []
    for char in text.upper():
        if char in morse_code:
            morse.append(morse_code[char])
        else:
            morse.append('')
    return ' '.join(morse)  

if __name__ == "__main__":
    input_text = input("text: ")
    morse_code_result = morsecode_conversion(input_text)
    print("Morse Code:", morse_code_result)
