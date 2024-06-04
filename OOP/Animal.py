class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

    def hacer_sonido(self):
        print(f"El animalito {self.nombre} hace: {self.sonido}!")

    