
class punto():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def eje_x(self):
        return self.x
    
    def eje_y(self):
        return self.y
    
    def imprimir(self):
        print('('+str(self.x)+', '+str(self.y)+')')
        
    def opuesto(self):
        return punto(-self.x, -self.y)
    
p = punto(2, 3)
q = p.opuesto()

p.imprimir()
q.imprimir()