def filtraMultiplos(lista,num):
    '''Função que filtra os múltiplos de um número n, retornando todos os elementos que forem divisíveis por n.'''
    multiplos = []
    proximo = 0
    while proximo<len(lista):
        if lista[proximo]%num == 0:
            multiplos = multiplos + [lista[proximo],]
        proximo = proximo + 1
    return multiplos