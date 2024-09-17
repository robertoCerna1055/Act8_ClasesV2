print("Clases version 2 el constructor")

class Perro:
    # Funcion constructor
    def __init__(self, color, edad):
        self.color = color
        self.edad = edad

    # Funciones creadas por el usuario

    def muerde(self):
        print("Me mordio")

    def chatperro(self, mensaje):
        print(f"Chat perro: {mensaje}")

    def chatcanina(self, mensaje):
        print(f"Chat canina: {mensaje}")

    def datos(self):
        print(f"Color: {self.color}, Edad: {self.edad}")

# Crear el objeto

chihuas = Perro("Negro",2)

# Llamadas a funciones

chihuas.datos()
chihuas.muerde()
chihuas.chatperro("Hola canina")
chihuas.chatcanina("Hola canino")
chihuas.chatperro("Quieres ser mi gugguu ?")
chihuas.chatperro("Grrrrru....")


