
# Ethan Cleary
def encode(password):
    global enc_password
    enc_password = ''
    for num in password:
        new_num = str(int(num) + 3)
        enc_password = enc_password + new_num
    return enc_password




while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")

    option = int(input("Please enter an option: "))

    if option == 1:
        password = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")
        print("")
    elif option == 2:
        print(f"The encoded password is {encode(password)}, and the original password is {decode(password)}.")
        print("")
    elif option == 3:
        break

def encode(password):
    global enc_password
    enc_password = ''
    for num in password:
        new_num = str(int(num) + 3)
        enc_password = enc_password + new_num
    return enc_password



