# coding: utf-8
'''
Created on 28/09/2014

@author: Mrguyfawkes
'''
import random
import templado
from collections import Counter

from random import randint
#CLASES PRINCIPALES
class Salon:
    def __init__(self, capacidad, numero, horario):
        self.horario = horario
        self.capacidad=capacidad
        self.numero=numero
        
class Materia:
    def __init__(self, nombre, horasSemanales, cantidadEstudiantes):
        self.cantidadEstudiantes = cantidadEstudiantes
        self.nombre = nombre
        self.horasSemanales = horasSemanales
        self.ultimoDia = -1
         
class Dia:
    def __init__(self, listaMaterias,j):    
        self.listaMaterias = listaMaterias
        self.nombre = j
    def printDia(self):
        if self.nombre==1:
            print ("Lun:\t"),
        elif self.nombre==2:
            print ("Mar:\t"),
        elif self.nombre==3:
            print ("Mie:\t"),
        elif self.nombre==4:
            print ("Jue:\t"),
        elif self.nombre==5:
            print ("Vie:\t"),
        for i in range(len(self.listaMaterias)):
            print self.listaMaterias[i].nombre,"\t",
        print ""
         
class Horario:
    def __init__(self, listaDias):
        self.listaDias = listaDias
    def printHorario(self):
        for i in range(len(self.listaDias)):
            self.listaDias[i].printDia()

#LLENAR LAS MATERIAS CON UN NOMBRE (Nï¿½MERO ENTERO) Y HORAS SEMANALES (4 o 6 de forma aleatoria)
def llenarMaterias(numMaterias):
    materias = []
    for j in range (1,numMaterias+1):
        cantidadEstudiantes = 0
        if j<30:
            cantidadEstudiantes = random.gauss(35, 5)
        elif j>=30 and j<60:
            cantidadEstudiantes = random.gauss(30,5)
        else:
            cantidadEstudiantes = random.gauss(80, 15)
        horasSem = 4
        materias.append(Materia(j, horasSem, cantidadEstudiantes))
#     for i in range(len(materias)):
#         print(materias[i].nombre)
    return materias
#Mï¿½todo que crea una lista de 6 materias    
def llenarDia(materias, dia, numMaterias):
    listaMaterias=[]
    for i in range (6):
        if  len(materias)>0:
            matAleat=randint(1, len(materias))
            #print(materias[matAleat-1].nombre, " horas sem ",materias[matAleat-1].horasSemanales)
            if materias[matAleat-1].horasSemanales > 0 and materias[matAleat-1].ultimoDia!= materias[matAleat-1].ultimoDia-1 and materias[matAleat-1].ultimoDia!=dia:
                materias[matAleat-1].ultimoDia = dia
                materias[matAleat-1].horasSemanales=materias[matAleat-1].horasSemanales-2
                if materias[matAleat-1].horasSemanales >0:
                    listaMaterias.append(materias[matAleat-1])
                else:
                    listaMaterias.append(materias.pop(matAleat-1))
    return Dia(listaMaterias,dia)
def crearHorario(materias, numMaterias):
    dias = []
    #SE LLENA UNA LISTA DE Dï¿½AS CON LISTAS DE MATERIAS
    for i in range(1,6):
        dias.append(llenarDia(materias,i, numMaterias))
    horario = Horario(dias)
    return horario
#LLENAR LOS SALONES CON UNA CAPACIDAD ALEATORIA Y UN Nï¿½MERO DE SALï¿½N I
def crearCalendario(materias, numSalones, numMaterias):
    salones = []
    for i in range (numSalones):
        if i<=2:
            capacidad = 35
        elif i>2 and i <=4 :#2 salones con capacidad de 40 estudiantes
            capacidad = 40
        elif i>4 and i<=6:#2 auditorios con capacidad de 100 estudiantes
            capacidad = 100
        else:
            capacidad = random.randint(20,40)
        horario = crearHorario(materias, numMaterias)
        salones.append(Salon(capacidad, i,horario))
    #imprimirCalendario(salones)
    return salones

def imprimirCalendario(calendario, n):
    print "-----------------  IMPRIMIENDO CALENDARIO: ", n , "---------------------------------"
    for i in range(len(calendario)):
        print "----------------SALON:", i+1,"---------------------"
        calendario[i].horario.printHorario()

def funcionObjetivoporCalendario(calendario):
    repeticiones = 0
    deltaCapacidades = 0
    temp = 0
    for val in Counter(countMaterias(calendario)).values():
        if val != 2:
            repeticiones += 1

    for i in range(len(calendario)):
        for j in range(len(calendario[i].horario.listaDias)):
            for k in range(len(calendario[i].horario.listaDias[j].listaMaterias)):
                deltaCapacidades = deltaCapacidades + abs(calendario[i].capacidad - calendario[i].horario.listaDias[j].listaMaterias[k].cantidadEstudiantes)
                temp= temp+1
    # deltaCapacidades= deltaCapacidades/temp
    z = deltaCapacidades + repeticiones
    return z
    
def cruzarCalendarios(calendarioA, calendarioB):
#     print ("CALENDARIO A --------")
#     imprimirCalendario(calendarioA)
#     print ("CALENDARIO B --------")
#     imprimirCalendario(calendarioB)
    
    for i in range(int(len(calendarioA)/2)):
        temp = calendarioA[i].horario
        temp2 = calendarioB[i].horario
        calendarioA[i].horario=temp2
        calendarioB[i].horario=temp

#     print ("CALENDARIO A --------")
#     imprimirCalendario(calendarioA)
#     print ("CALENDARIO B --------")
#     imprimirCalendario(calendarioB)
    
    return calendarioA, calendarioB
 
def mutacion(calendario):
    print "MUTACIÓN!!!!!!!!!!!!!!!!!!!!!"
    salonAleatorio = random.randint(0,len(calendario)-1)
    diaAleatorio = random.randint(0,len(calendario[salonAleatorio].horario.listaDias)-1)
    materiaAleatoria = random.randint(0,len(calendario[salonAleatorio].horario.listaDias[diaAleatorio].listaMaterias)-1)
    calendario[salonAleatorio].horario.listaDias[diaAleatorio].listaMaterias[materiaAleatoria].cantidadEstudiantes = random.randint(35, 100)
    
def buscarMejor(values):
    temp = values[0]
    indice = 0
    for i in range(len(values)):
        if values[i]<temp:
            temp = values[i]
            indice =  i
    return indice

def countMaterias(calendario):
    materias = []
    for salon in calendario:
        for dia in salon.horario.listaDias:
            materias += dia.listaMaterias
    
    for i in range(len(materias)):
        materias[i] = materias[i].nombre
    return materias

numSalones = 6 #6
numMaterias = 90 #90
generaciones =100
indiceMutacion = 0.0001
calendariosFinales= []
values = []
calendarios = []
# OPERADOR DE CRUCE !!!!!
#cruzarCalendarios(calendarioA, calendarioB)
#mutacion(calendarioA)
for i in range(10):
    calendarioA = crearCalendario(llenarMaterias(numMaterias), numSalones, numMaterias)
    calendarios.append(calendarioA)
    values.append(funcionObjetivoporCalendario(calendarioA))
print "--------TEMPLADO SIMULADO-----------"
print ""
print values
chosen = templado.simulated_annealing(values)
print "Mejor valor:", values[chosen[1]]
print ""
imprimirCalendario(calendarios[chosen[1]], "Elegido por templado")

print ""


for i in range(generaciones):
    #print(values)
    calendario1 = calendarios.pop(buscarMejor(values))
    values.pop(buscarMejor(values))
    calendario2 = calendarios.pop(buscarMejor(values))
    values.pop(buscarMejor(values))
    calendariosNuevos=[]
    calendariosNuevos.append(calendario1)
    calendariosNuevos.append(calendario2)
    while len(calendarios)>0:
        calendario3 = calendarios.pop(buscarMejor(values))
        values.pop(buscarMejor(values))
        calendario4 = calendarios.pop(buscarMejor(values))
        values.pop(buscarMejor(values))
#         aleat = random.randint(0,len(calendarios)-1)
#         calendario3 = calendarios.pop(aleat)
#         aleat2 = random.randint(0,len(calendarios)-1)
#         calendario4 = calendarios.pop(aleat2)
        A, B = cruzarCalendarios(calendario3, calendario4)
        calendariosNuevos.append(A)
        calendariosNuevos.append(B)
    
    #calendario11, calendario21 = cruzarCalendarios(calendario1, calendario2)
    values= []
    for i in range(len(calendariosNuevos)):
        values.append(funcionObjetivoporCalendario(calendariosNuevos[i]))
#     values.append(funcionObjetivoporCalendario(calendario21))
#     calendariosNuevos.append(calendario11)
#     calendariosNuevos.append(calendario21)
    calendarios = calendariosNuevos
    for i in range (10):          
        probMutacion = random.random()
        if probMutacion<= indiceMutacion:
            mutacion(calendarios[i])
        #values[i] = funcionObjetivoporCalendario(calendarios[i])
#for i in range (10):
#     print(calendarios[i].horario.listaDias[0].listaMaterias[0].cantidadEstudiantes, "<----- longitud")          
#    imprimirCalendario(calendarios[i], i+1)

print ""
#for calendario in calendarios:
#    print Counter(countMaterias(calendario))

print "--------ALGORITMO GENÉTICO------------"
print ""
print(values)
print "Mejor valor:", values[buscarMejor(values)]
print ""
imprimirCalendario(calendarios[buscarMejor(values)], "Elegido por algoritmo genético")
