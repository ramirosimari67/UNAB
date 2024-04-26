class Cancion:
    
    #Constructor
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    #Metodos para obtener el titulo y el autor
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    #Metodos para establecer el titulo y el autor
    def set_titulo(self, titulo):
        self.titulo = titulo
        
    def set_autor(self, autor):
        self.autor = autor

#Funcionamiento del codigo
if __name__ == '__main__':
    #Creo una instancia de Cancion
    mi_cancion = Cancion('Amor con Hielo', 'Morat')
    
    #Obtengo y muestro el titulo y el autor
    print('Titulo:', mi_cancion.get_titulo())
    print('Autor:', mi_cancion.get_autor())
    
    #Cambio el titulo y el autor
    mi_cancion.set_titulo('Hoja en blanco')
    mi_cancion.set_autor('Dread Mar I')
    
    #Muestro el titulo y el autor actualizados
    print('Titulo actualizado:', mi_cancion.get_titulo())
    print('Autor actualizado:', mi_cancion.get_autor())