#Start your python function here
def filtra_pares(tupla):
    '''Função recebe um tupla numeros inteiros e retorna um nova tupla com so com numeros pares'''
    pares = []
    for numeros in tupla:
        if numeros %2 == 0:
            pares.append(numeros)
    return tuple(pares)