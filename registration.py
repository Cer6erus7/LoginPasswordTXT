import utilities


help = """/register, /login, /help, /end"""

print(help)
while True:
    lobby = input('Type command here - ')
    if lobby == '/help':
        print(help)
    elif lobby == '/register':
        while True:
            login = input('Type your login - ')
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
