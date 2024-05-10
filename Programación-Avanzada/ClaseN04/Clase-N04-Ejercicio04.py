"""
Ejercicio 4: Definir una funcion denominada imprimo_fecha que reciba tres cadenas de caracteres como parametros formales, que representan un dia,
un mes y un año e imprima la fecha de la siguiente manera: "21 de septiembre de 2021".
"""
    
def imprimo_fecha():
    dia = input("Ingrese el dia: ")
    mes = input("Ingrese el mes: ")
    año = input("Ingrese el año: ")
    fecha = dia + ' de ' + mes + ' de ' + año
    return fecha

print(imprimo_fecha())