def Encrypt():
    shift = int(input("What Do You Want To Shift By?"))
    f = open("file.txt" , "r")
    text = f.read()
    new_text = ""
    for letter in text:
        lower = letter.islower()
        ascii_letter = ord(letter)
        if lower:
            if ascii != 95:
                new_text = new_text + chr((ascii_letter - 97 + shift) % 26 + 97)
            else:
                new_text = new_text + chr(32)
        else:
            if ascii != 95:
                new_text = new_text + chr((ascii_letter - 65 + shift) % 26 + 65)
            else:
                new_text = new_text + chr(32)
    print(new_text)


def decrypt():
    f = open("file.txt" , "r")
    text = f.read()
    new_text = ""
    for shift in range(26):
        for letter in text:
            lower = letter.islower()
            ascii_letter = ord(letter)
            if lower:
                if ascii != 95:
                    new_text = new_text + chr((ascii_letter - 97 + shift) % 26 + 97)
                else:
                    new_text = new_text + chr(32)
            else:
                if ascii != 95:
                    new_text = new_text + chr((ascii_letter - 65 + shift) % 26 + 65)
                else:
                    new_text = new_text + chr(32)
        print(new_text)
        new_text = ""
        print(new_text)


e_or_d = input("Do You Want To Encrypt Or Decrypt?")
if e_or_d == "Encrypt":
    Encrypt()
else:
    decrypt()
