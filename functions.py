from sqlite3 import Cursor
import mysql.connector

conn = mysql.connector.connect(host="localhost", port="3306", user="pyshop", password="pyshop", database="pyshop")
cursor = conn.cursor()


'''ДОБАВЛЕНИЕ КЛИЕНТА'''

def addClient(firstName, lastName, phone, money):
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

def addProduct(productName, productWeight, productPrice):
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
    print("Список клиентов: ")
    try:
        cursor.execute('SELECT * FROM tClient')
        record = cursor.fetchall()
        print("==================")
        for row in record:
            print("Имя: ", row[1])
            print("Фамилия: ", row[2])
            print("Телефон: ", row[3])
            print("Кошелек: ", row[4], "$")
            print("==================")
    except:
        print("В наличии нет ни одного клиента!")


'''СПИСОК ПРОДУКТОВ'''

def listProducts():
    print("Список продуктов: ")
    try:
        cursor.execute('SELECT * FROM tProduct')
        record = cursor.fetchall()
        print("==================")
        for row in record:
            print("Название: ", row[1])
            print("Вес: ", row[2], "г")
            print("Цена: ", row[3], "$")
            print("==================")
    except:
        print("В наличии нет ни одного продукта!")


'''ПОКУПКА'''

def Buy():
    print("Покупка продуктов: ")
    print("===================")
    listProducts()
    chooseProduct = int(input("Выберите продукт: "))
    cursor.execute('SELECT productID FROM tProduct')
    record = cursor.fetchall()
    for row in record:
        if chooseProduct == row[0]:
            print("")
            break
        else:
            print("===================")
            print("Нет такого продукта!")
            print("===================")
            return

    print("===================")
    listClients()
    chooseClient = int(input("Выберите клиента: "))
    cursor.execute('SELECT clientID FROM tClient')
    record = cursor.fetchall()
    for row in record:
        if chooseClient == row[0]:
            print("")
            break
        else:
            print("===================")
            print("Нет такого клиента!")
            print("===================")
            return
    
    
    
