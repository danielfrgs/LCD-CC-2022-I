# Ejercicio 3
# Elabora otro proceso p2 que calcule el cubo de el mismo conjunnto de números
# nums y mandalos a escribir

def calc_cuad(numeros):
    print('Calcula el cuadrado de los números')
    for n in numeros:
        print('Cuadrado: ', n * n)



def calc_cub(numeros):
    print('Calcula el cubo de los números')
    for n in numeros:
        print('Cubo: ', n*n*n)


nums = range(10)
if __name__ == '__main__':
    p2 = mp.Process(target=calc_cub, args=(nums,))
    p1 = mp.Process(target=calc_cuad, args=(nums,))
    p1.start()
    p2.start()
    
    p2.join()
    p1.join()
    


print('Termina la ejecución númerica de el intercalado')
