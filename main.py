#ENTRADA DE TEXTO
import numpy as np

with open('pesos.txt') as f:
    line1 = f.readline() #lee linea de vector de ciudades
    line2 = f.readline() #lee ciudad inicial   
    line3 = f.readline() #lee ciudad final

aux = line1.strip()
ciudades = aux.split(",") #vector con ciudades
num = len(ciudades)
initial_state = line2.strip()
final_state = line3.strip()

accesos = np.loadtxt("pesos.txt", delimiter=',', skiprows=4, max_rows=num)
#lee primera matriz (distancias entre ciuadades)
#print(accesos)

distancias_lineal = np.loadtxt("pesos.txt", delimiter=',', skiprows=5+num, max_rows=num)
#lee segunda matriz de distancias en linea recta
#print(distancias_lineal)


ruta=[] 
visitado = []

#Tentiva de formato de los estados
class State:
    def __init__(self,actual,ruta):                           #Las posibles rutas que se pueden tomar(lista de estados)
        self.actual = actual                            #Nombre del lugar actual  (Un string con el nombre)
        self.ruta = ruta   
    #Ciudades por las que a pasado , para ir en un solo sentido por asi decirlo (Una lista con los nombres de la ciudades)

class Action:
    def __init__(self,nombre_c):                          #Guarda la siguiente ciudad
      self.nombre_c=nombre_c                             #Nombre de la siguiente ciudad
   

def transition(state,action) :
  state.ruta.append(state.actual)                  #Guarda la ciudad anterior
  state.actual=action.nombre_c                            #Se actuliza la ciudad actual        
  
def is_final_state(state):
  if state.actual == final_state : 
      state.ruta.append(state.actual)
      return True      #Revisa si el nombre de la ciudad actual es igual a la destino
  return False

def get_valid_actions(state):                       #Entrega las ciudades disponibles 
    valid_actions = []
    i=ciudades.index(state.actual)
    for j in range (len(ciudades)): 
      if accesos[i][j]== 0 : continue
      
      aux = Action(ciudades[j])
      valid_actions.append(aux)
      
    return valid_actions

def visited(state):
  for ciudad in visitado:
    if ciudad == state.actual : return True
  return False

  
def visit(state):
  visitado.append(state.actual) 

#==================CODIGO A EJECUTAR===================================
from copy import deepcopy

initial=State(initial_state,ruta)

def bfs(initial_state):
  print("ENTRA anchura\n")
  
  solutions = []
  queue = [deepcopy(initial_state)]

  iters = 0
  while len(queue)>0:
    iters += 1
    state = queue.pop(0) #retorna y elimina primer elemento
    if is_final_state(state): 
      solutions.append(state)
      return state,iters

    actions = get_valid_actions(state)
    visit(initial_state)
    for action in actions:
      new_state = deepcopy(state) #ojo que debemos copiar el estado antes de modificarlo!
      transition(new_state, action)
      if visited(new_state):continue
      queue.append(new_state) #agrega al final
        
      visit(new_state)
      
  return solutions #se encontró una solución!


initial=State(initial_state,ruta)

def dfs(initial):
  print("ENTRA profundidad\n")
  
  solutions = []
  stack= [deepcopy(initial)]
  visitado.clear()
  iters = 0
  while len(stack)>0:
    iters += 1
    state = stack.pop(0) #retorna y elimina primer elemento
    if is_final_state(state): 
      solutions.append(state)
      return state,iters

    actions = get_valid_actions(state)
    visit(initial)
    for action in actions:
      new_state = deepcopy(state) #ojo que debemos copiar el estado antes de modificarlo!
      transition(new_state, action)
      if visited(new_state):continue
      stack.append(new_state) #agrega al final
      visit(new_state)
      
  return solutions #se encontró una solución!

  
#Funciones heuristicas
def heuristic_evalu(state):
  i=ciudades.index(state.actual)
  j=ciudades.index(final_state)
  
  aux_dis=accesos[i][j]
  aux_rec=distancias_lineal[i][j]
  auxs=aux_rec + aux_dis
  
  return auxs

from queue import PriorityQueue


initial=State(initial_state,ruta)


def astar(initial):
  print("ENTRA A*\n")
  q = PriorityQueue()
  q.put( (-1, deepcopy(initial)))

  visitado.clear()
  iters = 0
  while not q.empty():
    iters += 1
    elem=q.get()
    state = elem[1] #retorna y elimina el primer elemento


    if is_final_state(state): return state,iters #se encontró una solución!

    actions = get_valid_actions(state)
    
    visit(initial)
    for action in actions:
      new_state = deepcopy(state) #ojo que debemos copiar el estado antes de modificarlo!
 
      transition(new_state,action)

      if visited(new_state):continue
    
      visit(new_state)
      q.put((heuristic_evalu(new_state), new_state)) #agrega al final


  
#EJECUCUCIÓN DE SOLUCIONES
solucionA,itersA=bfs(initial)   
print("solucion",solucionA.ruta,"iteraciones",itersA,"\n")

solucionp,itersp=dfs(initial)   
print("solucion",solucionp.ruta,"iteraciones",itersp,"\n")

solucion,iters=astar(initial)
print("solucion",solucion.ruta,"iteraciones",iters)

