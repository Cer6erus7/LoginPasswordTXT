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


if __name__ == "__main__":
    register('Matvey', '12342')
    print(chek_login('Matvey'))