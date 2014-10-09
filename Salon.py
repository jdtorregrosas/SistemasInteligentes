'''
Created on 28/09/2014

@author: Mrguyfawkes
'''
import random
from random import randint
#CLASES PRINCIPALES
class Salon:
    def __init__(self, capacidad, numero):
        self.capacidad=capacidad
        self.numero=numero
        
class Materia:
    def __init__(self, nombre, horasSemanales):
        self.nombre = nombre
        self.horasSemanales = horasSemanales
        self.horasAsignadas = 0
         
class Dia:
    def __init__(self, listaMaterias):    
        self.listaMaterias = listaMaterias
         
class Horario:
    def __init__(self, listaDias):
        self.listaDias = listaDias
#VARIABLES NECESARIAS
numSalones = 2
numMaterias = 5
salones = []
materias = []
dias = []
#LLENAR LOS SALONES CON UNA CAPACIDAD ALEATORIA Y UN NÚMERO DE SALÓN I
for i in range (1,numSalones+1):
    capacidad = random.randint(20,30)
    salones.append(Salon(capacidad, i))
    
#LLENAR LAS MATERIAS CON UN NOMBRE (NúMERO ENTERO) Y HORAS SEMANALES (4 o 6 de forma aleatoria)
for j in range (1,numMaterias+1): 
    if random.random()<0.6 :
        horasSem = 4
    else:
        horasSem = 6
    materias.append(Materia(j, horasSem))

#Método que crea una lista de 6 materias    
def llenarDia():
    listaMaterias=[]
    for i in range (1,8):
        matAleat=randint(1, numMaterias)
        #print(matAleat-1)
        if materias[matAleat-1].horasAsignadas!= materias[matAleat-1].horasSemanales:
            listaMaterias.append(materias[matAleat-1])
            materias[matAleat-1].horasAsignadas=materias[matAleat-1].horasAsignadas+2
        else:            
            matAleat= randint(1, numMaterias)    
            i = i - 1
    return listaMaterias
#SE LLENA UNA LISTA DE DÏAS CON LISTAS DE MATERIAS
for i in range(1,6):
    dias.append(llenarDia())
    
#SE CREA UN HORARIO CON LA LISTA DE DÏAS (esto puede no ser necesario)
horario = Horario(dias)