def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


# Encode function
def encoder(encode):
    string = str(encode)
    encoded_pw = ""
    for x in string:
        encoded_pw += str((int(x) + 3) % 10)
    return int(encoded_pw)


# decode function
def decoder(decode):
    pass


if __name__ == "__main__":
    while True:
        menu()
        user_option = int(input("Please enter an option: "))
        if user_option == 1:
            password = input("Please enter your password to encode: ")
            encoder(password)
            print("Your password has been encoded and stored!")
        if user_option == 2:
            pass
        if user_option == 3:
            break
