import utilities


help = """/register, /login, /help, /end"""
point = True
log_login = None
print(help)


while point:
    lobby = input('Type command here - ')

    if lobby == '/help':
        print(help)

    elif lobby == '/register':
        while True:
            login = input('Type your new login - ')
            password = input('Type your password - ')
            password1 = input('Type your password again - ')
            if utilities.chek_login(login):
                if password1 == password:
                    utilities.register(login, password)
                    print("Success!")
                    break
                else:
                    print('Passwords are different! Try again!')
            else:
                print("Login is already exist! Try again!")

    elif lobby == "/login":
        while True:
            login = input("Type your login - ")
            password = input('Type your password - ')
            if utilities.get_login_password(login, password):
                print("You are in!\n")
                point = False
                log_login = login
                break
            else:
                print("Your date is incorrect! Try again")

    elif lobby == '/end':
        print('GoodBye!')
        point = False

    else:
        print("Command is incorrect!")



if log_login:
    print(utilities.loged_login(log_login))