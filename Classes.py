#Composicion de clases
import random
class Banda:
    def __init__(self):
        self.musicos = []
        self.instrumentos = [Guitarra(),Saxofon(), Tiple()]
        self.amigos = ['Max', 'Checo', 'Carlos','Charles','Oscar', 'Lando']

    def armar_banda(self, cantidad_musicos):
        for i in range(cantidad_musicos):
             self.musicos.append(Musico(random.choice(self.amigos)))
             self.musicos[-1].asignar_instrumento(random.choice(self.instrumentos))

    def mostrar_banda(self):
        for i in self.musicos:
              print(i.name," ",end="")
              i.instrumento.mostrar()
           

class Musico:
        def __init__(self,name):
              self.name = name
              self.instrumento = None
        
        def asignar_instrumento(self, instrumento):
              self.instrumento = instrumento

        def afinar_instrumento(self):
             self.instrumento.afinar()

        def tocar_instrumento(self):
             self.instrumento.tocar()           


class Instrumento:
    def __init__(self):
         pass
    def afinar(self):
         pass
    def tocar(self):
         pass
    def mostrar(self):
         print(str(type(self)).split('.')[-1][:-2])

class Saxofon(Instrumento):
        
        def afinar(self):
            print('Afinando')

        def tocar(self):
            
            print('tocando') 

class Guitarra(Instrumento):
        
        def afinar(self):
            print('Afinando')

        def tocar(self):
            
            print('tocando') 

class Tiple(Instrumento):
      
        def afinar(self):
            print('Afinando')

        def tocar(self):
            
            print('tocando') 

#p = ['Saxofon',"Guitarra", 'Bateria', 'Triangulo', 'Flauta', 'Piano', 'Trompeta','Violin', 'Bajo', 'Chelo']
#instrumentos = [Instrumento(i) for i in p]
"""Lista de instancias para la banda
alt click permite trabajar en mas de una linea a la vez
control+A  en el codigo, permite seleccionar todo el codigo a la vez
descargar imagenes 32x32 de asteroid"""
