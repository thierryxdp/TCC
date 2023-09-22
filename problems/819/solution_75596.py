def filtraMultiplos(lista,n):
    '''Função que dado uma lista e um numero(n) retorna uma lista com os numero divisiveis 
    por n da lista dada
    lista,numero-> lista'''
    proximo = 0
    multiplos = []
    while proximo < len(lista):
        if lista[proximo]%n==0:
            multiplos = multiplos + (lista[proximo],)
            proximo = proximo + 1
    return multiplos