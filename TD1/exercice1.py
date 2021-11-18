
from multiprocessing import Process
class Fibonacci(Process):
    def __init__(self,n):
        super().__init__()
        self.n = n
    def run(self):
        tab = [0]*(self.n +1)
        tab [0] = 0
        tab [1] = 1

        print (self.n)
        for i in range (2,self.n+ 1):
            tab [i] = tab[i-1]+tab[i-2]
        print (tab)

if __name__ == "__main__":
    p=Fibonacci(5)
    p.start()
    p.join()
