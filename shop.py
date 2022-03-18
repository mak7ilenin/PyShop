from sqlite3 import Cursor
import mysql.connector
from functions import addClient, addProduct, listClients, listProducts, Buy, editProduct, editClient, goNext


conn = mysql.connector.connect(host="localhost", port="3306", user="pyshop", password="pyshop", database="pyshop")
cursor = conn.cursor()


operation = 0

while operation != 9:
    print("Выберите операцию: ")
    print("1 - Добавить покупателя")
    print("2 - Список покупателей")
    print("3 - Добавить продукт")
    print("4 - Список продуктов")
    print("5 - Купить продукт")
    print("6 - Изменить продукт")
    print("7 - Имзенить покупателя")
    print("8 - Добавить денег покупателю")
    print("9 - Выйти из программы")
    choose = int(input())
    
    if choose == 1:
        addClient()
        goNext()

    elif choose == 2:
        listClients()
        goNext()
          
    elif choose == 3:      
        addProduct()
        goNext()
    
    elif choose == 4:
        listProducts()
        goNext()

    elif choose == 5:
        Buy()
        goNext()

    elif choose == 6:
        editProduct()
        goNext()

    elif choose == 7:
        editClient()
        goNext()

    elif choose == 8:
        print("Добавить бабки: ")
        addMoney = int(input())

    elif choose == 9:
        print("Вы вышли")
        break