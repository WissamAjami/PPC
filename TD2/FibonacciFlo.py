
from multiprocessing import Process
import os
import sys
import time
 
class Fibonacci(Process):
    def __init__(self, index):
        super().__init__()
        self.index = index
    def run(self):
        if self.index >= 0:
            print("pid : " + str(os.getpid()))
            print("ppid (pid du père) : " + str(os.getppid()))
            fibonacciList = [0, 1]
            for i in range (2, self.index + 1, 1):
                fibonacciList.append(fibonacciList[i-1] + fibonacciList[i-2])
            # voir avec commande ps aux | grep td1
            time.sleep(8)
        else:
            raise(IndexError)
 
if __name__ == "__main__":
    if len(sys.argv) > 1: # aqui verifica que tenga mas de 1 argumento, es decir aue exista un arg[0] y un arg[1]
        print("pid : " + str(os.getpid()))
        
        arg = sys.argv[1]
        try:
            index = int(arg)

        except:
            raise(os.error)
        p = Fibonacci(index)
        p.start()
        p.join()
    else:
        raise(ValueError)
