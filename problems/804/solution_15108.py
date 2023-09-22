def filtra_pares(tupla):
    '''Função que recebe uma tupla com 4 elementos e retorna outra tupla contendo apenas os elementos pares'''
    tuple = e1,e2,e3,e4
    pares = ()
    if tupla[0]%2 == 0:
        pares = tupla[0]
    if tupla[1]%2 == 0:
        pares2= tupla[1]
        pares = pares + pares2
    if tupla[2]%2 == 0:
        pares3 = tupla[2]
        pares = pares + pares3
    if tupla[3]%2 == 0:
        pares4 = tupla[3]
        pares = pares + pares4
    return pares