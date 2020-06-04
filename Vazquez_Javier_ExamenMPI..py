# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:45:24 2020

@author: javier
"""
import time
from mpi4py import MPI
from random import randint
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
np.random.RandomState(100)


filas=4000000
#filas=20
minimum=4
maximum=8
arr = np.random.randint(0, 10, size=[filas, 10])

#ar = arr.tolist()
start = time.time()
if rank == 0:  
    
    averow = int(filas/(size-1))
    extra = filas%(size-1)
    offset = 0
    
    for dest in range(1,size):
        rows = averow+1 if dest <= extra else averow 
        comm.send(offset, dest)
        comm.send(rows, dest)
        comm.send(arr[offset:(rows+offset)],dest)
        offset+=rows
    
    resultado=[]
    for i in range(1,size):
        extracto=comm.recv(source=i)
        
        resultado.append(extracto)
    
    
if rank > 0:
    offse=comm.recv(source=0)
    row=comm.recv(source=0)
    data=comm.recv(source=0)
    #print(data)
    res=[]
    for i in data:
        count = 0
        for j in i:
            if minimum <= j <= maximum:
                count += 1
        res.append(count)
    comm.send(res,0)
    
end=time.time()-start
print("Tiempo ",end)
