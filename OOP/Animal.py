class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
        self.vacuna = False

    def hacer_sonido(self):
        print(f"El animalito {self.nombre} hace: {self.sonido}!")

    def poner_vacuna(self):
        print(f"Vacunaste a {self.nombre}")
        self.vacuna = True
    #metodo en blanco|se define en cada clase que es lo que hace
    def ir_baño(self):
        raise NotImplementedError