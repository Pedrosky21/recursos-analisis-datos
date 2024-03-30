#Clase Persona con nombre, apellido y edad

class Persona:
    def __init__(self, nombre, apellido, edad, tareas=[], casado=False):
        self.nombre = nombre
        self.apellido = apellido
        self.__edad = edad #atributo privado, 
        # solo podra cambiarse su valor la primera vez, no dara error si se intenta mas veces pero no se cambiara
        self.casado = casado
        self.tareas = tareas

    def __str__(self): #Si no se define el comportamiento, al hacer un print se muestra la direccion de memoria donde esta el objeto
        estado_civil = "Soltero"
        if self.casado:
            estado_civil = "Casado"
        return f"{self.nombre} {self.apellido} | Edad: {self.__edad} | Estado Civil: {estado_civil}"
    
    def tareasPorRealizar(self):
        return len(self.tareas) > 0

pedro = Persona("Pedro", "Arreguez", 22)
print(pedro)

tareas_pendientes = "No"
if pedro.tareasPorRealizar():
    tareas_pendientes = "Si"

print("Quedan tareas por realizar? " + tareas_pendientes)