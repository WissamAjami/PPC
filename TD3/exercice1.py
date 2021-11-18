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
        
    def getPi(self):
        return pi
    
    def dansCercle(self, x, y):
        return (x**2 + y**2)<=1 
    
    def run(self):
        # print("...creation thread...")
        global pi, total
        pi = 0
        numerateur = 0
        denomminateur = n

        for i in range(n): 
            x =  random.random()
            y =  random.random()
            if (self.dansCercle(x, y)) :
                numerateur = numerateur + 1
        pi = 4*(numerateur/denomminateur)
        # print(pi)
        

if __name__=="__main__": 
    index = range(0,100)
    l=[]
    total = 0
    for t in index:
        t = howMuchPi(5000)
        t.start()
        t.join()
        l.append(t.getPi())
        total += t.getPi()


    print(total/100)

        
