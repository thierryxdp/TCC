def filtraMultiplos(lista,n):
    '''função que recebe uma lista de inteiros e um inteiro
    e retorna uma lista nova contendo todos os inteiros multi-
    plos de n.
    list, int -> list
    '''
    multiplos = []
    indice = 0
    while indice < len(lista):
        if lista[indice]%n==0:
            multiplos += [lista[indice]]
        indice += 1
    return multiplos