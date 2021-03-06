#encoding:UTF-8
#Autor: Lenin Silva Gutiérrez, A01373214
#Programa que grafica vectores en Graphics

from Graphics import *
import math

#dibuja el plano cartesiano de referencia
def dibujarPlano(x,y,t):
    t.pen.color=Color("green")
    t.penDown()
    t.forward(x/2)
    t.moveTo(0,y/2)
    t.moveTo(x/2,y/2)
    t.moveTo(x/2,0)
    t.moveTo(x/2,y)
    t.moveTo(x/2,y/2)
    t.penUp()

#hace que la tortuga rote contrario a las manecillas del reloj
def rotarTortuga(grados,t):
    t.rotate(grados)
    return

#dibuja el vector de aceurdo a una magnitud y oreintación dada        
def dibujarVector(magnitud, grados,t):
    rotarTortuga(grados,t)#llama a la función que hace girar a la flecha
    t.pen.color=Color("yellow")
    t.penDown()
    t.forward(magnitud)
    t.penUp()
    return
    
#obtiene los componentes 'x' y 'y' del vector y regresa su valor    
def obtenerComponentes(grados, magnitud,x,y):
    comp_x=x/2+(magnitud*math.cos(math.radians(grados)))
    comp_y=y/2-(magnitud*math.sin(math.radians(grados)))
    return comp_x, comp_y    
    
#dibuja el cuadrado que encierra al vector dibujado    
def dibujarCuadrado(magnitud, grados,x,y,t):
    t.pen.color=Color("red")
    t.penDown()
    #obtiene con una función previamente cosntruida los valores de las componentes 'x' y 'y' y los asigna a variables  
    comp_x,comp_y=obtenerComponentes(grados,magnitud,x,y)
    t.moveTo(x/2, comp_y)#dibuja el trazo paralelo al eje x
    t.penUp()
    t.moveTo(comp_x, y/2)
    t.penDown()
    t.moveTo(comp_x,comp_y)#dibuja el trazo paralelo al eje y
    return
    
def main():
    magnitud=int(input("Magnitud del vector"))
    grados=int(input("Grados del vector (desde x positivo contrario a las manecillas del reloj)"))
    v=Window("Vector",800,800)
    v.setBackground(Color("black"))#establece el color del fondo en negro
    t=Arrow((400,400),0)
    t.draw(v)
    dibujarPlano(800,800,t)
    dibujarVector(magnitud, grados,t)
    dibujarCuadrado(magnitud, grados,800,800,t)
    t.penUp()
    t.moveTo(400,400)
    return
    
main()
    
    