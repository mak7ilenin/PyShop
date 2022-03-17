import array as arr
from sqlite3 import Cursor
import mysql.connector
from client import Client
from product import Product


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
        phone = int(input())

        print("Введите бабки: ")
        money = int(input())

        with open(clientFile, "a") as file:
            file.write(firstName + "\n" + lastName + "\n" + str(phone) + "\n" + str(money) + "\n")

            
    elif choose == 2:
        print("Список клиентов: ")
        # # clientLine = file.readline()
        # with open("client.txt", "r") as q:
        #     for i in q:
        #         print("Имя: ",i)
        


           
    elif choose == 3:
        print("Введите название продукта: ")
        productName = input()
        
        print("Введите вес товара: ")
        productWeight = int(input())

        print("Введите цену: ")
        productPrice = int(input())
        
        with open(clientFile, "a") as file:
            file.write(productName + "\n" + str(productWeight) + "\n" + str(productPrice) + "\n")

    elif choose == 5:
        print("Добавить бабки: ")
        addMoney = int(input())
        sumMoney = addMoney + money
        print(sumMoney)

    elif choose == 7:
        print("Вы вышли")
        break
    

# cl = Client(firstName, lastName, phone, money)
# cl.printClient()

# productName = input()
# productPrice = int(input())
# productWeight = int(input())

# pr = Product(productName, productPrice, productWeight)
# pr.printProduct()





# cursor.execute('''
#                 INSERT INTO client (firstName, lastName, phone, money)
#                 values
#                 ("dsf"),("dfsdf"),(2342),(432)
#                 ''')
# cursor.execute('CREATE TABLE tClient(firstName varchar(25) not null, lastName varchar(25) not null, phone varchar(8) not null, money float not null)')
# cursor.execute('INSERT INTO tClient (firstName, lastName, phone, money) values("dsf"),("dfsdf"),(2342),(432)')
# conn.commit()
# conn.close()
# for i in cursor:
#     print(i)
# print(cl.firstName, cl.money, cl.phone, cl.money)
