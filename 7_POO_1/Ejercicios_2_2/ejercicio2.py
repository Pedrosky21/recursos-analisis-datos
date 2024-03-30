class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cant_patas = cantidad_patas
        self.tipo = tipo
    
    def comer():
        return "Estoy comiendo"


class Perro(Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza
    
    def correr():
        return "Estoy corriendo"


class Aguila(Animal):
    def volar():
        return "Estoy volando"
