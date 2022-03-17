class Client:
    def __init__(self, firstName, lastName, phone, money):
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.money = money
    def printClient(self):
        print("Имя клиента: ", self.firstName, "Фамилия: ", self.lastName, "Телефон: ", self.phone, "Деньги: ", self.money)