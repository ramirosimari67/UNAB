"""
Ejercicio 7: Definir una función que calcule el área de un círculo, otra que calcule el área de un rectángulo y otra que calcule el área de un cuadrado.
Analice qué parámetros deberían recibir dichas funciones.
"""
#Metodo para calcular el area de un circulo
def area_circulo(self, radio):
    self.radio = radio
    
    area = 3.1416*radio**2
    return area
radio = float(input("Ingrese el radio del circulo: "))
print("El area del circulo es: ", area_circulo(radio))

# Metodo para calcular el area de un rectangulo
def area_rectangulo(self, base, altura):
    self.base = base
    self.altura = altura

    area = base * altura
    return area
base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))
print("El area del rectangulo es: ", area_rectangulo(base, altura))

# Metodo para calcular el area de un cuadrado
def area_cuadrado(self, lado):
    self.lado = lado
    
    area = lado * lado
    return area

lado = float(input("Ingrese la longitud de un lado del cuadrado: "))
print("El area del cuadrado es: ", area_cuadrado(lado))