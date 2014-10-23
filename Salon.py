# coding: utf-8
'''
Created on 28/09/2014

@author: Mrguyfawkes
'''
import random
import Templado

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

#LLENAR LAS MATERIAS CON UN NOMBRE (Nï¿½MERO ENTERO) Y HORAS SEMANALES (4 o 6 de forma aleatoria)
def llenarMaterias(numMaterias):
    materias = []
    for j in range (1,numMaterias+1):
        cantidadEstudiantes = 0
        if j<30:
            cantidadEstudiantes = random.gauss(35, 5)
        elif j>=30 & j<60:
            cantidadEstudiantes = random.gauss(30,5)
        else:
            cantidadEstudiantes = random.gauss(80, 15)
        horasSem = 4
        materias.append(Materia(j, horasSem, cantidadEstudiantes))
    return materias
#Mï¿½todo que crea una lista de 6 materias    
def llenarDia(materias, dia, numMaterias):
    listaMaterias=[]
    for i in range (1,8):
        matAleat=randint(1, len(materias))
        #print(matAleat-1)
        if materias[matAleat-1].horasSemanales > 0:
            listaMaterias.append(materias[matAleat-1])
            materias[matAleat-1].horasSemanales=materias[matAleat-1].horasSemanales-2
        else:            
            matAleat= randint(1, numMaterias)    
            i = i - 1
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
        elif i>2 & i <=4 :#2 salones con capacidad de 40 estudiantes
            capacidad = 40
        elif i>4 & i<=6:#2 auditorios con capacidad de 100 estudiantes
            capacidad = 100
        else:
            capacidad = random.randint(20,40)
        horario = crearHorario(materias, numMaterias)
        salones.append(Salon(capacidad, i,horario))
    #imprimirCalendario(salones)
    return salones

def imprimirCalendario(calendario, n):
    print "-------  IMPRIMIENDO CALENDARIO: ", n , "--------"
    for i in range(len(calendario)):
        print "----------------------------------SALON:", i+1,"------------------------------------"
        calendario[i].horario.printHorario()

def funcionObjetivoporCalendario(calendario):
    horasTotales = 0
    deltaCapacidades = 0
    temp = 0
    for i in range(len(calendario)):
        for j in range(len(calendario[i].horario.listaDias)):
            for k in range(len(calendario[i].horario.listaDias[j].listaMaterias)):
                horasTotales = horasTotales + calendario[i].horario.listaDias[j].listaMaterias[k].horasSemanales
                deltaCapacidades = deltaCapacidades + abs(calendario[i].capacidad - calendario[i].horario.listaDias[j].listaMaterias[k].cantidadEstudiantes)
                temp= temp+1
    deltaCapacidades= deltaCapacidades/temp
    z= deltaCapacidades + horasTotales
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
    salonAleatorio = random.randint(0,len(calendario)-1)
    diaAleatorio = random.randint(0,len(calendario[salonAleatorio].horario.listaDias)-1)
    materiaAleatoria = random.randint(0,len(calendario[salonAleatorio].horario.listaDias[diaAleatorio].listaMaterias)-1)
    calendario[salonAleatorio].horario.listaDias[diaAleatorio].listaMaterias[materiaAleatoria].cantidadEstudiantes = random.randint(30, 100)
    
numSalones = 2
numMaterias = 90
calendarioA = crearCalendario(llenarMaterias(numMaterias), numSalones, numMaterias)
calendarioB = crearCalendario(llenarMaterias(numMaterias), numSalones, numMaterias)
# OPERADOR DE CRUCE !!!!!
#cruzarCalendarios(calendarioA, calendarioB)
#mutacion(calendarioA)
values = []
calendarios = []
for i in range(10):
    calendarioA = crearCalendario(llenarMaterias(numMaterias), numSalones, numMaterias)
    calendarios.append(calendarioA)
    values.append(funcionObjetivoporCalendario(calendarioA))
#print(values)
#chosen = Templado.simulated_annealing(values)
#print(chosen)
#imprimirCalendario(calendarios[chosen[2]])

generaciones = 1000
indiceMutacion = 0.00001
calendariosFinales= []

def buscarMejor(values):
    temp = values[0]
    indice = 0
    for i in range(len(values)):
        if values[i]<temp:
            temp = values[i]
            indice =  i
    return indice
for i in range(generaciones):
    calendario1 = calendarios.pop(buscarMejor(values))
    values.pop(buscarMejor(values))
    calendario2 = calendarios.pop(buscarMejor(values))
    values.pop(buscarMejor(values))
    calendario11, calendario21 = cruzarCalendarios(calendario1, calendario2)
    calendariosNuevos=[]
    values= []
    values.append(funcionObjetivoporCalendario(calendario11))
    values.append(funcionObjetivoporCalendario(calendario21))
    calendariosNuevos.append(calendario11)
    calendariosNuevos.append(calendario21)
    for i in range(8):
        calendarioAleatorio = crearCalendario(llenarMaterias(numMaterias), numSalones, numMaterias)
        calendariosNuevos.append(calendarioAleatorio)
        values.append(funcionObjetivoporCalendario(calendarioAleatorio))
    calendarios = calendariosNuevos
for i in range (10):          
    probMutacion = random.random()
    if probMutacion<= indiceMutacion:
        mutacion(calendarios[i])
        #values[i] = funcionObjetivoporCalendario(calendarios[i])
for i in range (10):
    #print calendarios[i].horario.listaDias[0].listaMaterias[0].cantidadEstudiantes, "<----- longitud"          
    imprimirCalendario(calendarios[i], i+1)
    
    
    
    
