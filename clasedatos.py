class Informacion():

    def mi_Lista(self):
        lista_NomPerros = ["Firulais", "Coco", "Drako"]
        for x in lista_NomPerros:
            print(x)

    def mi_Tupla(self):
        tupla_RazaPerros = ("Chihuahua", "Pitbull", "Dañmata")
        for x in tupla_RazaPerros:
            print(x)

    def mi_Conjunto(self):
        conjunto_NomGatos = {"Kira", "Raspy", "Wilson"}
        for x in conjunto_NomGatos:
            print(x)

    def mi_Diccionario(self):
        diccionario_razaGatos = {
    "Slames": "Slames",
    "Abisinio": "Abisinio",
    "Persa": "Persa"
}
        
        for x in diccionario_razaGatos:
            print(x)

# Creando el objeto

datos = Informacion()
print()
print("LISTADO de nombres de perros")
datos.mi_Lista()

print()
print("TUPLA de razas de perros")
datos.mi_Tupla()

print()
print("CONJUNTO de nombres de gatos")
datos.mi_Conjunto()

print()
print("DICCIONARIO de razas de gatos")
datos.mi_Diccionario()
