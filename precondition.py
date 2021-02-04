import random
name = 'Alex'
surname = 'Testov'
telefon = '+79145555555'
pas = '1231t23'
confpas = '1231t23'
link = ''

def Mail():
    email = 'test' + str(random.randint(1, 2000)) + '@mail.ru'
    return  email

def Login():
    login = 'te' + str(random.randint(1, 2000))
    return login