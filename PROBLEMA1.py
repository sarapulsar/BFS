from random import randint # librerias
from queue import Queue
import hashlib
################Generador de Grafos
ORDER = 10
with open("Re.txt", "w+") as f:
    n = randint(7, ORDER)# Genera los nodos se tiene en cuenta el problema de los 6
    nEdges = randint(1, n * (n - 1) // 2) ##Genera los enlaces
    #f.write(f"{n}\n")
    print("Nodos",n)
    for i in range(1, nEdges):
        v1 = randint(0, n-1) 
        v2 = randint(0, n-1)
        while (v1==v2):
            v1 = randint(0, n-1) 
            v2 = randint(0, n-1)
            print("Error son iguales")   
        f.write(f"{v1} {v2}\n")
print("los enlaces",nEdges) 
    #f.write("0")
##### almacena en un nuevo archivo. Estoy depurando mi .txt para que no repita columnas
p=open("Re.txt")
pf=open("Rdepurado.txt","w")
#almacena
tmp=set()
for txt in p:
    if txt not in tmp:
        pf.write(txt)
        tmp.add(txt)
p.close()
pf.close()
f=open("Rdepurado.txt")
#print(f.read())
#f=f.read().split()
#f=f.read()
#################_ Diccionario
grafo={}
#print(f)
for i in f:
    columna=i.split()
    grafo.setdefault(columna[0],[]).append(columna[1])
    grafo.setdefault(columna[1],[]).append(columna[0])
print(grafo)
print(type(grafo)) # lista de adyacencias
####################_ BFS
nivel={}
padre={}
bfs_salida =[]
visitado={}
queue=Queue()
for node in grafo.keys():
    visitado[node]=False
    padre[node]= None # inicializar
    nivel[node]=-1# inicializar las variables
#print(visitado)
#print(padre)
#print(nivel)
S = list(grafo.keys())[0] #extrae el primer nodo de la lista.
visitado[S]=True
nivel[S]=0
queue.put(S) # se utiliza la colección queue
while not queue.empty():# se  examinan los vertices.
    u=queue.get()
    bfs_salida.append(u)# se saca un verice
    for v in grafo[u]:# se e
        if not visitado[v]: #Se actualiza
            visitado[v]=True
            padre[v]=u
            queue.put(v)
            nivel[v]=nivel[u]+1 
print("Ruta:",bfs_salida)
print("Niveles de cada vertice:",nivel)
#print(len(nivel))
if len(nivel)<=6: # si cumple o no cumple el grafo
    print("Ruta cumple la ley de los 6:",bfs_salida)
else: 
    print("No se puede comprobar la ley de los 6 grados con esta entrada: ",bfs_salida)