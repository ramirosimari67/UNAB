"""
Ejercicio 5: Definir una funcion denominada cuantos_dias que reciba el numero de mes como parametro y retorne la cantidad de dias que posee. 
Ejemplo: cuantos_dias(1), deberia retornar 31.
Ayuda: Pensar en tener una lista de la siguiente manera: [["enero",31], ["febrero",28], ...]
"""

def cuantos_dias(numero_mes):
    meses = [
        ['Enero', 31],
        ['Febrero', 28],
        ['Marzo', 31],
        ['Abril', 30],
        ['Mayo', 31],
        ['Junio', 30],
        ['Julio', 31],
        ['Agosto', 31],
        ['Septiembre', 30],
        ['Octubre', 31],
        ['Noviembre', 30],
        ['Diciembre', 31]
    ]
    
    for mes in meses:
        if mes[0] == numero_mes:
            return mes[1]
        
print(cuantos_dias('Enero'))
print(cuantos_dias('Febrero'))
