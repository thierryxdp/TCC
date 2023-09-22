def filtra_pares(tupla):
    ''' funcao que recebe uma tupla com quatro
    elementos inteiros e retorna uma nova tupla
    contendo apenas os elementos pares da tupla original
    tupla, int-->tupla,int'''
    pares = ()
    if (tupla [0] % 2) == 0:
        pares += (tupla[0],)
    if (tupla [1] % 2) == 0:
        pares += (tupla[0],)
    if (tupla [2] % 2) == 0:
        pares += (tupla[0],)
    if (tupla [3] % 2) == 0:
        pares += (tupla[0],)
    return pares