class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

juan = Persona("Juan Pallas", 25)
jaime = Persona ("Jaime Pallas", 26)

print (f"Juan se llama {juan.nombre} y tiene {juan.edad} años")
print (f"Jaime se llama {jaime.nombre} y tiene {jaime.edad} años")