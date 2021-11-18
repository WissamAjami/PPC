# exercice1.py
# encodage
# imports
import sys 
from threading import Thread 
import random


class howMuchPi(Thread):
    def __init__(self, nombre):
        Thread.__init__(self)
        global n
        n = nombre
        pi = 0
    
    
    def dansCercle(x, y):
        return (x**2 + y**2)<=1 
    
    def run(self):
        print("...creation thread...")
        global pi
        pi = 0
        nummerateur = 0
        denomminateur = n
        total = 0
        for i in range(n): 
            x =  random.random()
            y =  random.random()
            if (dansCercle(x,y)) :
                nummerateur = nummerateur + 1
        pi = 4*(nummerateur/denomminateur)
        total = total + pi 
        print(self.dansCercle(1,1))

if __name__=="__main__":
    
    for i in range(100):
        t = howMuchPi(5)
        t.start()
        t.join()
        ##val = val + t.pi
    ##val = val / 100

    ##print (val)

