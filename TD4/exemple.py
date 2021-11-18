import time
import random
import multiprocessing
 
def fibonacci(n):
    print(multiprocessing.current_process().name)
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a+b
        i += 1
    return (n, a)
 
if __name__ == "__main__":
    indexes = [random.randint(0, 100) for i in range(10)]
 
    with multiprocessing.Pool(processes = 4) as pool:
        print("*** Synchronous call in one process")
        result = pool.apply(fibonacci, (20,))
        print(result)
 
        print("*** Asynchronous call in one process")
        result = pool.apply_async(fibonacci, (10,))
        print(result.get())
 
        print("*** Synchronous map")
        for x in pool.map(fibonacci, indexes):
            print(x)
 
        print("*** Asynchronous map")
        for x in pool.map_async(fibonacci, indexes).get():
            print(x)
 
        print("*** Deliberate timeout")
        result = pool.apply_async(time.sleep, (5,))
        print(result.get(timeout=1))