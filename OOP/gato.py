from Animal import Animal

#clase Hijo(Padre)
class Gato(Animal):
    def __init__(self, nombre, sonido, tipo_pelaje):
        super().__init__(nombre, sonido)
        self.tipo_pelaje = tipo_pelaje
    
    def rascar_sofa(self):
        print(f"{self.nombre} esta rescando el sofa")
    
    #polimorfismo / sobreescritura
    def hacer_sonido(self):
        print(f"El gato te ve, se aleja y dice {self.sonido}")

    def ir_baño(self):
        print("Va a su caja, razca la arena y va al baño")