# 6) Função filtra pares

def par(x):
    '''dado um número, retorna se ele é par(true) ou não(false).
    float -> bool'''
    if (x %2 == 0):
        return True
    else:
        return False

def filtra_pares(tupla):
    '''dada uma tupla de 4 elementos inteiros, retorna uma tupla com apenas os elementos
    pares da tupla original.
    tuple -> tuple'''
    a1 = int(tupla[0]) 
    a2 = int(tupla[1])
    a3 = int(tupla[2])
    a4 = int(tupla[3])
    elemento = ()
    if par(a1):
        elemento = elemento + (a1,)
    if par(a2):
        elemento = elemento + (a2,)
    if par(a3):
        elemento = elemento + (a3,)
    if par(a4):
        elemento = elemento + (a4,)
    return elemento