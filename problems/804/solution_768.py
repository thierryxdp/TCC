def filtra_pares(a,b,c,d):
    '''retorna uma nova tupla contendo apenas os elementos pares da dupla dada, dados numeros inteiros'''
    lista1 = (a,b,c,d)
    lista2 = sorted(filter(lambda x: x % 2 == 0, lista1))
    return lista2