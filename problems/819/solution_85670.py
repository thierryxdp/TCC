def filtraMultiplos(lista ,numero):
    '''funçao que dada uma lista de numeros e um numero retorna os multiplos desse numero que estao na lista
    list, int -> list'''
    indice = 0
    multiplos = []
    while indice < len(lista):
        resto = lista[indice]%numero
        indice += 1
        if resto == 0:
            multiplos += [lista[indice-1]]
    return multiplos