"""
Ejercicio 3: Definir una funcion denominada retorno_mensaje que retorno siguiente mensaje: "Estudiando Fundamento de Informatica en la UNAB".

A. ¿Cómo hago para mostrar ese mensaje en pantalla?
B. ¿Qué diferencia encuentra con el ejercicio anterior?
C. Si tuvieras que imprimir mensajes como “Estudiando Matemática I en la UNAB“ y “Estudiando Python en la UNAB” utilizando la misma función
¿Cómo la modificarías? 
"""

def retorno_mensaje():
    mensaje = "Estudiando Fundamento de Informatica en la UNAB.\n"
    mensaje += "Estudiando Matematica I en la UNAB.\n"
    mensaje += "Estudiando Python en la UNAB.\n"
    return mensaje

print(retorno_mensaje())