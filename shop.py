from sqlite3 import Cursor
import mysql.connector
from functions import addClient, addProduct, listClients, listProducts, Buy


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

        addClient(firstName, lastName, phone, money)
            
    elif choose == 2:
        listClients()
          
    elif choose == 3:
        print("Введите название продукта: ")
        productName = input()
        
        print("Введите вес товара в граммах: ")
        productWeight = float(input())

        print("Введите цену: ")
        productPrice = float(input())
        
        addProduct(productName, productWeight, productPrice)
    
    elif choose == 4:
        listProducts()

    elif choose == 5:
        print("Добавить бабки: ")
        addMoney = int(input())
        

    elif choose == 6:
        Buy()

    elif choose == 7:
        print("Вы вышли")
        break