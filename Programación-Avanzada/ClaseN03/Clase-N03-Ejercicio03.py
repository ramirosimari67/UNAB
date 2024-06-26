# Defino la clase punto
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Defino la clase linea
class Linea():
    def __init__(self, punto_inicio, punto_fin):
        self.punto_inicio = punto_inicio
        self.punto_fin = punto_fin
        
    # Creo los movimientos
    def mueve_derecha(self, distancia):
        self.punto_inicio.x += distancia
        self.punto_fin.x += distancia
        
    def mueve_izquierda(self, distancia):
        self.punto_inicio.x -= distancia
        self.punto_fin.x -= distancia
        
    def mueve_arriba(self, distancia):
        self.punto_inicio.y += distancia
        self.punto_fin.y += distancia
        
    def mueve_abajo(self, distancia):
        self.punto_inicio.y -= distancia
        self.punto_fin.y -= distancia
        
punto_inicio = Punto(3, 4)
punto_fin = Punto(5, 4)
linea = Linea(punto_inicio, punto_fin)

print("Punto de inicio:", (linea.punto_inicio.x, linea.punto_inicio.y))
print("Punto de fin:", (linea.punto_fin.x, linea.punto_fin.y))

linea.mueve_derecha(2)
print("Desplazamiento a la derecha:")
print("Punto de inicio:", (linea.punto_inicio.x, linea.punto_inicio.y))
print("Punto de fin:", (linea.punto_fin.x, linea.punto_fin.y))
