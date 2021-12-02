morse_translation = {
    "Q": "––•–",
    "W": "•––",
    "E": "•",
    "R": "•–•",
    "T": "–",
    "Y": "–•––",
    "U": "••–",
    "I": "••",
    "O": "–––",
    "P": "•––•",
    "A": "•–",
    "S": "•••",
    "D": "–••",
    "F": "••–•",
    "G": "––•",
    "H": "••••",
    "J": "•–––",
    "K": "–•–",
    "L": "•–••",
    "Z": "––••",
    "X": "–••–",
    "C": "–•–•",
    "V": "•••–",
    "B": "–•••",
    "N": "–•",
    "M": "––",

    "1": "•----",
    "2": "••---",
    "3": "•••--",
    "4": "••••-",
    "5": "•••••",
    "6": "-••••",
    "7": "--•••",
    "8": "---••",
    "9": "----•",
    "0": "-----",

    " ": "  "
}


def text_to_morse(convert_text):
    result = " "
    for letter in convert_text:
        if letter.upper() in morse_translation:
            input_text = morse_translation[letter.upper()]
            result += input_text + " "
        else:
            pass
    return result


def morse_to_text(morse_code):
    result = " "
    morse_input = morse_code.split("  ")
    for morse_word in morse_input:
        morse_letters = morse_word.split(" ")
        for morse_letter in morse_letters:
            for key, value in morse_translation.items():
                if value == morse_letter:
                    result += key
        result += " "

    return result


keep_running = True
while keep_running:
    choice = input("Welcome to our Morse Converter World!\n"
                   "Type: \n"
                   "1) To encode into Morse Code\n"
                   "2) To decode into Text\n")

    if choice == "1":
        text = input("Type Text(s) to convert\n")
        t_convert = text_to_morse(text)
        print(t_convert)
    elif choice == "2":
        m_code = input("Type Morse Code to convert\n")
        m_convert = morse_to_text(m_code)
        print(m_convert)

    restart = input("Would you like to continue?\n"
                    "Type Y or N\n").upper()
    if restart == "N":
        keep_running = False
        print("Thank you for using our Morse Converter, GOODBYE!")
