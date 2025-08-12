class Persona:
    def __init__(self, altura, peso, edad):
        self.altura = altura
        self.peso = peso
        self.edad = edad

    def imc(self):
        return self.peso / (self.altura ** 2)


altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
edad = int(input("Ingrese su edad: "))

persona = Persona(altura, peso, edad)

imc = persona.imc()
print (imc)
if imc <= 18.5:
    print("El resultado del cálculo del IMC indica que la persona tiene bajo peso")
elif imc >= 30:
    print("La persona es obesa")
else:
    print("La persona tiene sobre peso o una complexión normal")
