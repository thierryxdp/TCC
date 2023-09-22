def filtraMultiplos (lista, numero):
    '''Função que retorna uma lista contendo os múltiplos de um numero
    list, int -> list'''
    multiplos = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%numero == 0:
            multiplos = multiplos + [lista[proximo],]
        proximo = proximo + 1
    return multiplos