#retorna uma tupla com apenas os valores pares da tupla informada
def filtra_pares(x):
    t = ()
    a = len(x)
    for z in range(a):
        if  x[z]%2 == 0:
            aux=x[z]
            t = t + (aux,)
    return t