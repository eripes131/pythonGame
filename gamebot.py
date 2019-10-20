import random

b = True
money = 100
chose = 0

if b == True:
    while chose != 3:
        print ('Выберите игру: \n1)Камень Ножницы Бумага \n2)Угадай Число \n3)Выход')
        chose = input()
        if int(chose) == 1:
            print ('Выберите предмет: \n1)Камень \n2)Ножницы \n2)Бумага')
            l = input()
            k = random.randint(1,3)
            if int(l) == 1 and k == 1:
                print ('Ничья! Противник выбрал Камень')
            if int(l) == 2 and k == 1:
                print ('Ты проиграл! Противник выбрал Камень')
            if int(l) == 3 and k == 1:
                print ('Ты выйграл! Противник выбрал Камень')
            if int(l) == 1 and k == 2:
                print ('Ты выйграл! Противник выбрал Ножницы')
            if int(l) == 2 and k == 2:
                print ('Ничья! Противник выбрал Ножницы')
            if int(l) == 3 and k == 2:
                print ('Ты проиграл! Противник выбрал Ножницы')
            if int(l) == 1 and k == 3:
                print ('Ты проиграл! Противник выбрал Бумагу')
            if int(l) == 2 and k == 3:
                print ('Ты выйграл! Противник выбрал Бумагу')
            if int(l) == 3 and k == 2:
                print ('Ничья! Противник выбрал Бумагу')
        if int(chose) == 2:
            cat = 0
            print('Выберите категорию \n1)100 \n2)1000 \n3)10000')
            cat = input()
            if int(cat) == 1:
                j = 0
                a = random.randint(1,100)
                print('Введите число!')
                while j != a:
                    j = input()
                    if int(j) > a:
                        print('Число мнеьше!')
                    if int(j) < a:
                        print('Число больше!')
                    if int(j) == a:
                        print('Ты выйграл! Загаданое число было: ' + str(a))
            if int(cat) == 2:
                j = 0
                a = random.randint(1,1000)
                print('Введите число!')
                while j != a:
                    j = input()
                    if int(j) > a:
                        print('Число мнеьше!')
                    if int(j) < a:
                        print('Число больше!')
                    if int(j) == a:
                        print('Ты выйграл! Загаданое число было: ' + str(a))
            if int(cat) == 1:
                j = 0
                a = random.randint(1,10000)
                print('Введите число!')
                while j != a:
                    j = input()
                    if int(j) > a:
                        print('Число мнеьше!')
                    if int(j) < a:
                        print('Число больше!')
                    if int(j) == a:
                        print('Ты выйграл! Загаданое число было: ' + str(a))
        if int(chose) == 3:
            print('Спасибо за сеанс!')
            break 