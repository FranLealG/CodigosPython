class Persona:
    
    escuela = "Coding Dojo"
    lista_persona = []
    # init se encarga de inicializar  el objeto/ metodo constructor
    def __init__(self,name, last_name, e_mail, age):
        # codigo | luego de inicializar se le agregan los datos de la clase, elementos
        self.nombre = name
        self.apellido = last_name
        self.email = e_mail
        self.linas_codigo = 0 #lineas de codigo que se ha desarrollado
        self.edad = age

        Persona.lista_persona.append(self)

    #self: el objeto  que se esta inicializando| objeto que invoca a la funcion
    def imprimir(self):
        print(self.nombre, self.apellido, self.email)

    def saludar(self):
        print(f"Te saluda {self.nombre}: Holaa!")

    def codificar(self, cant_lineas):
        self.linas_codigo += cant_lineas

    @classmethod #metodo de clase
    def imprimir_todos(cls): #cls se refiere a la clase que invoca al metodo
        #cls = persona
        for p in cls.lista_persona:
            p.imprimir()

    @staticmethod #metodos estaticos | ayudantes|auxiliares
    def mayor_edad(edad):
        #mayor edad 22
        if edad < 18:
            return False
        else:
            return True
    
    def licencia_conducir(self):
        #mayor_edad(22)
        if Persona.mayor_edad(self.edad):
            print("puedes tener la licencia")
        else:
            print("aún no puedes tener tu licencia")