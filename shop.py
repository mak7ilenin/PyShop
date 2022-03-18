import array as arr
from sqlite3 import Cursor
import mysql.connector


conn = mysql.connector.connect(host="localhost", port="3306", user="pyshop", password="pyshop", database="pyshop")
cursor = conn.cursor()


operation = 0

while operation != 7:
    print("Выберите операцию: ")
    print("1 - Добавить покупателя")
    print("2 - Список покупателей")
    print("3 - Добавить продукт")
    print("4 - Список продуктов")
    print("5 - Добавить денег клиенту")
    print("6 - Купить продукт")
    print("7 - Выйти из программы")
    choose = int(input())
    clientFile = "client.txt"
    if choose == 1:
        print("Введите имя: ")
        firstName = input()
        
        print("Введите фамилию: ")
        lastName = input()
        
        print("Введите мобилу: ")
        phone = input()

        print("Введите бабки: ")
        money = float(input())

        # with open(clientFile, "a") as file:
        #     file.write(firstName + "\n" + lastName + "\n" + str(phone) + "\n" + str(money) + "\n")

        try:
            cursor.execute('CREATE TABLE tClient(clientID int identity primary key not null, firstName varchar(25) not null, lastName varchar(25) not null, phone varchar(8) not null, money float not null)')
            conn.commit()
        except:
            print("")
        try:
            cursor.execute("INSERT INTO tClient VALUES (%s, %s, %s, %s)", (firstName, lastName, phone, money))
            conn.commit()
            print("Пользователь", firstName, lastName, "добавлен в базу")
            print("=======================================")
        except:
            print("Авария! Нет электричества! Ждём!")
            
    elif choose == 2:
        print("Список клиентов: ")
        try:
            cursor.execute('SELECT * FROM tClient')
            record = cursor.fetchall()
            print("==================")
            for row in record:
                print("Имя: ", row[0])
                print("Фамилия: ", row[1])
                print("Телефон: ", row[2])
                print("Кошелек: ", row[3], "$")
                print("==================")
        except:
            print("В базе нет ни одного клиента!")
          
    elif choose == 3:
        print("Введите название продукта: ")
        productName = input()
        
        print("Введите вес товара в граммах: ")
        productWeight = float(input())

        print("Введите цену: ")
        productPrice = float(input())
        
        try:
            cursor.execute('CREATE TABLE tProduct(productName varchar(25) not null, productWeight float not null, productPrice float not null)')
            conn.commit()
        except:
            print("")
        try:
            cursor.execute("INSERT INTO tProduct VALUES (%s, %s, %s)", (productName, productWeight, productPrice))
            conn.commit()
            print(productName, "добавлен в базу")
            print("=======================================")
        except:
            print("Авария! Нет электричества! Ждём!")
    
    elif choose == 4:
        print("Список продуктов: ")
        try:
            cursor.execute('SELECT * FROM tProduct')
            record = cursor.fetchall()
            print("==================")
            for row in record:
                print("Название: ", row[0])
                print("Вес: ", row[1], "г")
                print("Цена: ", row[2], "$")
                print("==================")
        except:
            print("В базе нет ни одного продукта!")

    elif choose == 5:
        print("Добавить бабки: ")
        addMoney = int(input())
        sumMoney = addMoney + money
        print(sumMoney)

    elif choose == 7:
        print("Вы вышли")
        break