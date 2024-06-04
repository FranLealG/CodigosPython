class Producto:
    def __init__(self, nombre, numid, precio, categoria,stock):
        self.nombre = nombre
        self.numid = numid
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
    
    def imprimir(self):
        print(self.nombre, self.numid, self.precio, self.categoria)
    
    def stock(self):
        print(f"El stock de {self.nombre} es de: {self.stock}")