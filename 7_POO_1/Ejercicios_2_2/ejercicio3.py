import ejercicio1 as ej1

class Persona:
    def __init__(self, nombre, edad, profesion, actividad="Ninguna"):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        self.actividad = actividad # ninguna, trabaja, camina o anda en bicicleta
    
    def __str__(self) -> str:
        return self.nombre + " tiene " + str(self.edad) + " y es de profesión " + self.profesion + "."

juan = Persona("Juan Lopez", 25, "Abogado")
bicicleta = ej1.Bicicleta("Massino", 2000, "Amarillo", True)

print(juan, " Por la tarde, después de trabajar, sale a caminar. También tiene una bicicleta de color", bicicleta.color, 
      "marca", bicicleta.marca, "y a veces sale a dar vueltas en ella.")
