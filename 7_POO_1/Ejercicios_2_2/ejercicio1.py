class Bicicleta:
    def __init__(self, marca, precio, color, usada=False):
        self.marca = marca
        self.precio = precio
        self.color = color
        self.usada = usada
    
    def __str__(self):
        return "La bicicleta es de la marca " + self.marca + ", de color " + self.color + " y cuesta $" + str(self.precio)
    
    def esta_usada(self):
        mensaje = "No está usada"
        if (self.usada):
            mensaje = "Está usada"
        return mensaje
    
    def precio_mayor(self, precio):
        return self.precio > precio
