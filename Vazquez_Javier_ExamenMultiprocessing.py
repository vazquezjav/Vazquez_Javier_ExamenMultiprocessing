# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:44:35 2020

@author: javier
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:53:11 2020

@author: javier
"""
import time

import numpy as np


import multiprocessing
import random
import time

class Examen(multiprocessing.Process):
    def __init__(self, queue,minimum,maximum,arr,inicio,fin):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.minimum=minimum
        self.maximum=maximum
        self.arr=arr
        self.inicio=inicio
        self.fin=fin
        self._return=None

    def run(self) :
        
        for i in range(self.inicio,self.fin):
            #print(self.arr[i])
            self.queue.put(self.how_many_within_range_sequential(self.arr[i],self.minimum,self.maximum))
            
        self._return=self.queue
        return self._return
    
        
    def how_many_within_range_sequential(self,row, minimum, maximum):   
        
        count = 0
        for n in row:
            if minimum <= n <= maximum:

                count += 1
        
        return count

if __name__ == '__main__':


    np.random.RandomState(100)

    arr = np.random.randint(0, 10, size=[4000000, 10])

    ar = arr.tolist()

    start = time.time()

    resultsSec = []
    minimum=4
    maximum=8
    
    res=[]
    queue = multiprocessing.Queue()
    queue2 = multiprocessing.Queue()
    examen = Examen(queue,minimum,maximum,arr,0,round(len(arr)/2))
    examen.start()
    examen.join()
    for i in range(queue.qsize()):
        res.append(queue.get())
    examen2 = Examen(queue2,minimum,maximum,arr,round(len(arr)/2),round(len(arr)))
    
    examen2.start()
    examen2.join()
    

    for i in range(queue2.qsize()):
        res.append(queue2.get())
    print(len(res))
    end =  time.time()-start
    print("Tiempo: ",end)

   
