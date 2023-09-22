def filtraMultiplos(lista, n):
    '''Retorna uma lista contendo os números da lista inserida que são multiplos de n; list[int], int -> list[int]'''
    multiplos=[]
    indice=0
    while indice<len(lista):
        if lista[indice]%n=0:
            multiplos=multiplos+lista[indice]
        indice=indice+1
    return multiplos