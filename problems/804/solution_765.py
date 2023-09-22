def filtra_pares(a,b,c,d):
    '''retorna uma nova tupla contendo apenas os elementos pares da dupla dada, dados numeros inteiros'''
    lista_nova = []
    lista1 = (a,b,c,d)
    return sorted(filter(lambda x: x % 2 == 0, lista1)):