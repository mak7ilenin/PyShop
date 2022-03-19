from sqlite3 import Cursor
import mysql.connector
from mysqlx import RowResult

conn = mysql.connector.connect(host="localhost", port="3306", user="pyshop", password="pyshop", database="pyshop")
cursor = conn.cursor()


'''ВОЗВРАЩЕНИЕ В МЕНЮ'''

def goNext():
    print("\n=========================")
    print("Вернуться в меню?")
    goNext = int(input("1 - да // 2 - выйти: "))
    print("========================")
    if goNext == 1:
        print("")
    else:
        quit()


'''ДОБАВЛЕНИЕ КЛИЕНТА'''

def addClient():
    print("Введите имя: ")
    firstName = input()
    
    print("Введите фамилию: ")
    lastName = input()
    
    print("Введите мобилу: ")
    phone = input()

    print("Введите бабки: ")
    money = float(input())
    
    try:
        cursor.execute('CREATE TABLE tClient(clientID int AUTO_INCREMENT primary key, firstName varchar(25) not null, lastName varchar(25) not null, phone varchar(8) not null, money float not null)')
        conn.commit()
    except:
        print("")
    try:
        cursor.execute("INSERT INTO tClient VALUES (null, %s, %s, %s, %s)", (firstName, lastName, phone, money))
        conn.commit()
        print("Пользователь", firstName, lastName, "добавлен в базу")
        print("=======================================")
    except:
        print("Авария! Нет электричества! Ждём!")
        print("==================================")


'''ДОБАВЛЕНИЕ ПРОДУКТА'''

def addProduct():
    print("Введите название продукта: ")
    productName = input()
    
    print("Введите вес товара в граммах: ")
    productWeight = float(input())

    print("Введите цену: ")
    productPrice = float(input())
    try:
        cursor.execute('CREATE TABLE tProduct(productID int AUTO_INCREMENT primary key, productName varchar(25) not null, productWeight float not null, productPrice float not null)')
        conn.commit()
    except:
        print("")
    try:
        cursor.execute("INSERT INTO tProduct VALUES (null, %s, %s, %s)", (productName, productWeight, productPrice))
        conn.commit()
        print(productName, "добавлен в магазин")
        print("=======================================")
    except:
        print("Авария! Нет электричества! Ждём!")


'''СПИСОК КЛИЕНТОВ'''

def listClients():
    print("Список пользователей: ")
    try:
        cursor.execute('SELECT * FROM tClient')
        record = cursor.fetchall()
        print("==================================================================================")
        for row in record:
            print("Пользователь номер -", row[0])
            print("Имя: ", row[1], "//", "Фамилия: ", row[2], "//", "Телефон: ", row[3], "//", "Кошелек: ", row[4], "$")
            print("==================================================================================")
    except:
        print("В наличии нет ни одного клиента!")


'''СПИСОК ПРОДУКТОВ'''

def listProducts():
    print("Список продуктов: ")
    try:
        cursor.execute('SELECT * FROM tProduct')
        record = cursor.fetchall()
        print("==================================================================================")
        for row in record:
            print("Продукт номер -", row[0])
            print("Название: ", row[1], "//" , "Вес: ", row[2], "г", "//", "Цена: ", row[3], "$")
            print("==================================================================================")
    except:
        print("В наличии нет ни одного продукта!")


'''ПОКУПКА'''

def Buy():
    print("Покупка продуктов")
    print("===================")
    listProducts()

    '''НАХОЖДЕНИЕ ПРОДУКТА ПО ЕГО ID И СРАВНИВАНИЕ С ВЫБОРОМ ПРОГРАММЫ'''
    chooseProduct = int(input("Выберите продукт: "))
    cursor.execute('SELECT productID FROM tProduct')
    record = cursor.fetchall()
    for row in record:
        if chooseProduct == row[0]:
            print("")
            break

    print("===================")
    listClients()   
    
    '''НАХОЖДЕНИЕ КЛИЕНТА ПО ЕГО ID И СРАВНИВАНИЕ С ВЫБОРОМ ПРОГРАММЫ'''
    chooseClient = int(input("Выберите клиента: "))
    cursor.execute('SELECT clientID FROM tClient')
    record = cursor.fetchall()
    for row in record:
        if chooseClient == row[0]:
            print("")
            break
    
    '''НАХОЖДЕНИЕ ДЕНЕГ КЛИЕНТА ПО ЕГО ID '''

    listChooseClient = [chooseClient]
    try:
        cursor.execute('SELECT money FROM tClient WHERE clientID = %s', (listChooseClient))
        record = cursor.fetchall()
    except:
        print("Ошибка!")
        return
    for row in record:
        clientMoney = row[0]


    '''НАХОЖДЕНИЕ ДЕНЕГ ПРОДУКТА ПО ЕГО ID '''
    
    listChooseProduct = [chooseProduct]
    try:
        cursor.execute('SELECT productPrice FROM tProduct WHERE productID = %s', (listChooseProduct))
        record = cursor.fetchall()
    except:
        print("Ошибка!")
        return
    for row in record:
        productPrice = row[0]

    cursor.execute('SELECT * FROM tProduct WHERE productID = %s', (listChooseProduct))
    record = cursor.fetchall()
    for row in record:
        print("==================================================================================")
        print("Название: ", row[1], "//" , "Вес: ", row[2], "г", "//", "Цена: ", row[3], "$")
        print("==================================================================================\n")
    print("Купить этот продукт?")
    booleanAnswer = int(input("1 - да // 2 - нет: "))
    if booleanAnswer == 1:
        if clientMoney >= productPrice:
            purchaseMoney = clientMoney - productPrice
            cursor.execute('UPDATE tClient SET money = %s WHERE tClient.clientID = %s', (purchaseMoney, chooseClient))
            conn.commit()
            print("")
            print("===========================")
            print("Покупка совершена успешно!")
            print("Текущий остаток: ", purchaseMoney, "$")
        else:
            print("")
            print("======================")
            print("Недостаточно средств!")
            print("======================")
            return
    else:
        print("Авария! Нет электричества! Ждём!")
        return


'''ИЗМЕНЕНИЕ ПРОДУКТА'''

def editProduct():
    print("Изменение продукта")
    print("===================")
    listProducts()
    print("Выберите продукт, который хотите изменить: ")
    chooseEditProduct = int(input())
    try:
        cursor.execute('SELECT productID from tProduct')
        record = cursor.fetchall()
    except:
        print("Нет такого продукта!")
        return
    for row in record:
        if chooseEditProduct == row[0]:
            break

    listChooseEditProduct = [chooseEditProduct]
    cursor.execute('SELECT * FROM tProduct WHERE productID = %s', (listChooseEditProduct))
    record = cursor.fetchall()
    for row in record:
        print("==================================================================================")
        print("Название: ", row[1], "//" , "Вес: ", row[2], "г", "//", "Цена: ", row[3], "$")
        print("==================================================================================\n")
    print("Изменить этот продукт?")
    booleanAnswer = int(input("1 - да // 2 - нет: "))
    if booleanAnswer == 1:
        print("Изменить название товара: ")
        editProductName = input()
        
        print("Изменить вес товара в граммах: ")
        editProductWeight = float(input())

        print("Изменить цену товара: ")
        editProductPrice = float(input())

        try:
            cursor.execute("UPDATE tProduct SET productName = %s, productWeight = %s, productPrice = %s WHERE tProduct.productID = %s", (editProductName, editProductWeight, editProductPrice, chooseEditProduct))
            conn.commit()
        except:
            print("Изменение не удалось!")
            return
        print("\n=====================================================")
        print("Измененный продукт:", editProductName, "//", editProductWeight, "//", editProductPrice)


'''ИЗМЕНЕНИЕ КЛИЕНТА'''

def editClient():
    print("Изменение пользователя")
    print("===================")
    listClients()
    print("Выберите пользователя, которого хотите изменить: ")
    chooseEditClient = int(input())
    cursor.execute('SELECT clientID from tClient')
    record = cursor.fetchall()
    for row in record:
        if chooseEditClient == row[0]:
            print("")
            break
    
    listChooseEditClient = [chooseEditClient]
    try:
        cursor.execute('SELECT * FROM tClient WHERE clientID = %s', (listChooseEditClient))
        record = cursor.fetchall()
    except:
        print("Нет такого пользователя!")
        return
    for row in record:
        print("=====================================================================================")
        print("Имя: ", row[1], "//", "Фамилия: ", row[2], "//", "Телефон: ", row[3], "//", "Кошелек: ", row[4], "$")
        print("=====================================================================================\n")
    print("Изменить этого пользователя?")
    booleanAnswer = int(input("1 - да // 2 - нет: "))
    if booleanAnswer == 1:
        print("Введите новое имя: ")
        editFirstName = input()
       
        print("Введите новую фамилию: ")
        editLastName = input()
        
        print("Введите новую мобилу: ")
        editPhone = input()

        print("Изменить бабки: ")
        editMoney = float(input())

        try:
            cursor.execute("UPDATE tClient SET firstName = %s, lastName = %s, phone = %s, money = %s WHERE tClient.clientID = %s", (editFirstName, editLastName, editPhone, editMoney, chooseEditClient))
            conn.commit()
        except:
            print("")
            print("Изменение не удалось!")
            return
        print("\n===========================================================================")
        print("Измененный пользователь:", editFirstName, "//", editLastName, "//", editPhone, "//", editMoney, "$")