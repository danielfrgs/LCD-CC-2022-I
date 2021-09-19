import multiprocessing as mp
import time

nums_res = []

def calc_cuad(numeros):
    global nums_res
    for n in numeros:
        print('cuadrado:', n * n )
        nums_res.append(n * n)
        
    #print("Resultado del proceso:", nums_res)    

    
nums = range(10)

t = time.time()
p1 = mp.Process(target=calc_cuad, args=(nums,))

p1.start()
p1.join()

print("Tiempo de ejecución: ", time.time()-t)
print("Resultado del proceso:", nums_res)    
print("Finaliza ejecución")
