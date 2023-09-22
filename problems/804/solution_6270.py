'''Filtra os numeros pares de uma tupla
int,int,int,int-->int'''
def filtra_pares(lista):
    pares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
    return tuple(pares)