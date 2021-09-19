import multiprocessing as mp


def tarea(cadena):
    print('Hola', cadena)


if __name__ == '__main__':
    p = mp.Process(target=tarea, args=('Lucas',))
    p.start()

# --------------------------
# Ejemplo 2


def calc_cuad(numeros):
    print('Calcula el cuadrado de los números')
    for n in numeros:
        print('Cuadrado: ', n * n)


nums = range(10)
if __name__ == '__main__':
    p1 = mp.Process(target=calc_cuad, args=(nums,))
    p1.start()
    p1.join()

print('Termina la ejecución númerica del Cuadrado')
