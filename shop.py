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
    money = int(500)
    
    if choose == 1:
        print("Введите имя: ")
        firstName = input()
        print(firstName)
        
        print("Введите фамилию: ")
        secondName = input()
        print(secondName)
    elif choose == 3:
        print("Введите название продукта: ")
        productName = input()
        print(productName)
        
        print("Введите цену: ")
        productPrice = int(input())
        print(productPrice)
    elif choose == 5:
        print("Введите бабки: ")
        money = int(input())
        print(money)
    elif choose == 7:
        print("Вы вышли")
        break
    



