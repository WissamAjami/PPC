# primeOrNot.py 
# encodage
# imports
import random
import time
import math
import multiprocessing


def is_prime(n):
    if n < 2:
        return (n, False)
    if n == 2:
        return (n, True)
    if n % 2 == 0:
        return (n, False)
 
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return (n, False)
    return (n, True)



if __name__=="__main__":
    workers = 1
    indexes = [random.randint(10**3, 10**6) for i in range(1000000)]
    start = time.time()
    
    with multiprocessing.Pool(processes=workers) as pool: 
        print("*** Synchronous call in one process")
        # result = pool.apply(is_prime, (10,))
        # print(result)
        
        liste = pool.map(is_prime,indexes)
        print("======= De facon synchronne =======")
        # for entier in pool.map(is_prime,indexes):
        #     liste.append(entier)
        # print(liste)

    end = time.time()
    seconds = end - start
    
    
    print("Pour",len(indexes),"nombres et",workers,"process, le Temps mis est de", seconds)