#Composicion de clases
class Banda:
    def __init__(self):
        self.musico = None
    def armar_banda(self, musico):
        self.musico = musico


class Musico:
        def __init__(self):
              self.instrumento = None
        
        def asignar_instrumento(self, instrumento):
              self.instrumento = instrumento
        
class Instrumento:
    def __init__(self,name):
          self.name = name
    def afinar():
            print('Afinando')
    def tocar():
            print('tocando')  

p = ['Saxofon',"Guitarra", 'Bateria', 'Triangulo', 'Flauta', 'Piano', 'Trompeta','Violin', 'Bajo', 'Chelo']
instrumentos = [Instrumento(i) for i in p]
#for i in instrumentos:
 #     i.afinar()
