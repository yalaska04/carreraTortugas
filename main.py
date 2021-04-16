# programa que genera un carrera de tortugas
import turtle
import random

class Circuito():
    corredores = []
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ('red', 'blue', 'green', 'orange')
# Inicializamos la pantalla    
    def __init__(self, width, height):
# Me interesa que sea privado xq no quiero que nadie puedo modificarlo
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startline = -width/2 + 20
        self.__finishline = width/2 - 20
        
        self.__createRunners()
    
    def __createRunners(self): 
# Inicializamos las tortugas        
        for i in range(4):
            # mete en la lista corredores 4 tortugas 
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__startline, self.__posStartY[i])
            
            
            self.corredores.append(new_turtle)
    
    def competir(self):
        
        hayGanador = False
        
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1,6)
                tortuga.forward(avance)
                
                if tortuga.position()[0] >= self.__finishline:
                    hayGanador = True
                    print('la tortuga de color {} ha ganado'.format(tortuga.color()[0]))

        
if __name__ == '__main__':
    circuito = Circuito(640, 480)
    circuito.competir()
        
        
        