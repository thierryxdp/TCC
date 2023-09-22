def filtraMultiplos(lista,n):
    '''Filtra e retorna os múltiplos, do número n recebido, presentes na lista
    lista, int -> lista'''
    indice = 0
    multiplo = []
    while indice < len(lista):
        if lista[indice] % n == 0:
             list.append(multiplo,lista[indice])
        indice+= 1
    return multiplo