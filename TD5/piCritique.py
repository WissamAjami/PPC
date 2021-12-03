from threading import Thread
import random
import sys

class piCritique(Thread):
    r = 1
    def __init__(self, numberOfThreads):
        super().__init__()
        self.n = numberOfThreads
        
    def run(self):
        numerateur = 0
        n = self.n
        for a in range(n):
            x = int(random.random())
            y = int(random.random())
            if (self.dansCercle(x,y)):
                numerateur = numerateur+1
        pi = 4 *((numerateur)/(n))
        
        print(pi)
        
    def dansCercle(self,x,y):
        return x**2+y**2 <= self.r

if __name__=="__main__":
    index = int(sys.argv[1])
    t = piCritique(index)
    t.start()
    t.join()
