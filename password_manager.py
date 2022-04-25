master_password = input("what is the master password? ")


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
           data= line.rstrip()
           user,passw = data.split(':')
           print("User:",user,": Password:",passw)



def add():
    name = input("Account name: ")
    password = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + ": " + password + "\n")


while True:
    mode = input(
        "would you like to add a new password or view existing one? press q to quit"
    )
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode. ")
        continue
