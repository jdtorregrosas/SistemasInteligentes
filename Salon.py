# coding: utf-8
'''
Created on 28/09/2014

@author: Mrguyfawkes
'''
import random
from random import randint
#CLASES PRINCIPALES
class Salon:
    def __init__(self, capacidad, numero, horario):
        self.horario = horario
        self.capacidad=capacidad
        self.numero=numero
        
class Materia:
    def __init__(self, nombre, horasSemanales):
        self.nombre = nombre
        self.horasSemanales = horasSemanales
        self.horasAsignadas = 0
         
class Dia:
    def __init__(self, listaMaterias,j):    
        self.listaMaterias = listaMaterias
        self.nombre = j
    def printDia(self):
        if self.nombre==1:
            print ("lunes")
        elif self.nombre==2:
            print ("Martes")
        elif self.nombre==3:
            print ("Miercoles")
        elif self.nombre==4:
            print ("Jueves")
        elif self.nombre==5:
            print ("Viernes")
        for i in range(1, len(self.listaMaterias)):
            print (self.listaMaterias[i].nombre)
         
class Horario:
    def __init__(self, listaDias):
        self.listaDias = listaDias
    def printHorario(self):
        for i in range(0,len(self.listaDias)):
            self.listaDias[i].printDia()
#VARIABLES NECESARIAS
numSalones = 2
numMaterias = 35
salones = []
materias = []
#LLENAR LAS MATERIAS CON UN NOMBRE (N�MERO ENTERO) Y HORAS SEMANALES (4 o 6 de forma aleatoria)
for j in range (1,numMaterias+1): 
#     if random.random()<0.6 :
#         horasSem = 4
#     else:
    horasSem = 4
    materias.append(Materia(j, horasSem))
#M�todo que crea una lista de 6 materias    
def llenarDia(materias, dia):
    listaMaterias=[]
    for i in range (1,8):
        matAleat=randint(1, len(materias))
        #print(matAleat-1)
        if materias[matAleat-1].horasAsignadas!= materias[matAleat-1].horasSemanales:
            listaMaterias.append(materias[matAleat-1])
            materias[matAleat-1].horasAsignadas=materias[matAleat-1].horasAsignadas+2
        else:            
            matAleat= randint(1, numMaterias)    
            i = i - 1
    return Dia(listaMaterias,dia)
def crearHorario(materias):
    dias = []
    #SE LLENA UNA LISTA DE D�AS CON LISTAS DE MATERIAS
    for i in range(1,6):
        dias.append(llenarDia(materias,i))
    horario = Horario(dias)
    return horario
#LLENAR LOS SALONES CON UNA CAPACIDAD ALEATORIA Y UN N�MERO DE SAL�N I
for i in range (1,numSalones+1):
    if i<=2:#2 auditorios con capacidad de 100 estudiantes
        capacidad = 100
    elif i>2 & i <=4 :#2 salones con capacidad de 40 estudiantes
        capacidad = 40
    elif i>4 & i<=6:
        capacidad = 35
    else:
        capacidad = random.randint(20,40)
    horario = crearHorario(materias)
    salones.append(Salon(capacidad, i,horario))

for i in range(0,len(salones)):
    print ("----------------------------------SALON:", i+1,"------------------------------------")
    salones[i].horario.printHorario()

