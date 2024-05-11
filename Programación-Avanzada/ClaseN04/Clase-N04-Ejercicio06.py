"""
Ejercicio 6: Definir una funcion que reciba un numero como parametro y mostrar la tabla de multiplicar de dicho numero.
"""
# Defino la funcion multiplicar
def tabla_de_multiplicar():
    numero = int(input('Ingrese un numero para ver su tabla de multiplicar: '))
    print(f'Tabla de multiplicar del {numero}: ')
    for i in range(1, 11):
        resultado = numero * 1
        print(f'{numero} x {i} = {resultado}')
    
# Llama la funcion    
tabla_de_multiplicar()