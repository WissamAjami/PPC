# Fibonacci.py
# encodages
# imports
from multiprocessing import Process
import os



# code
class Fiboncci(Process):
    element : int
    def __init__(self, element = None): # element represente l'element de la suite qu'on veut atteindre
        super().__init__()
        if element == None:
            self.element = int(input("Elements : "))
        else :
            self.element = element


    def run(self):
        print("... creation processus ...")
        liste = [0, 1]
        for i in range (2, self.element):         
            liste.append(liste[i-1]+liste[i-2])
        print(liste, "child says: my processes is",os.getppid(), "and my parent process is", os.getppid())



if __name__ == "__main__":
    
    p = Fiboncci(8)
    p.start()
    p.join()
    print("Proces says my pid is ",os.getpid())
    