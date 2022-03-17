class Product:
    def __init__(self, productName, productPrice, productWeight):
        self.productName = productName
        self.productPrice = productPrice
        self.productWeight = productWeight

    def printProduct(self):
        print("Название продукта: " + self.productName + "Цена продукта: ", self.productPrice, "Вес прордукта: ", self.productWeight)