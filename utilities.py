def register(login, password):
    """
    Принимает логин и пароль пользователя, и записывает его в текстовой файл.
    :param login: str
    :param password: str
    :return: None
    """
    with open('db', 'a') as f:
        f.write(f"{login} {password}\n")


def chek_login(login):
    """
    Принимает логин и проверяет его на уникальность в файле, возвращает логическое значение.
    :param login:
    :return:
    """
    with open('db', 'r') as f:
        for i in f.readlines():
            logins = i.split()
            if logins[0] == login:
                return False
        return True

def get_login_password(login, password):
    """
    Принимает логин и пароль, и проверяет их в базе даных. Возвращает Правду, если логин
    и пароль есть в наличии, а если нет то, Ложь
    :param login:
    :param password:
    :return:
    """
    with open('db', 'r') as f:
        for i in f.readlines():
            lst = i.split()
            if lst[0] == login and lst[1] == password:
                return True
        return False


def loged_login(login):
    """
    Принимает логин и приветствует залогиневшегося клиента
    :param login:
    :return:
    """
    with open('db', 'r') as f:
        for i in f.readlines():
            lst = i.split()
            if lst[0] == login:
                return f"Hello {lst[0]}!"
        return "Login doesn't exist!"


if __name__ == "__main__":
    # register('Matvey', '12342')
    print(chek_login('Matvey'))
    print(get_login_password('Matvey', '1232'))
    print(loged_login('Matvey'))