from multiprocessing import Process, Manager


def f(n):
    fibonacciList = [0, 1]
 
if __name__ == '__main__':
    with Manager() as manager:
        

        p = Process(target=f, args=(n))
        p.start()
        p.join()
 
        print(n)
        print(p.fibonacciList) 