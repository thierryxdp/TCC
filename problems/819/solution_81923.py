def filtraMultiplos(lista,n):
    '''Função que calcula e retorna uma lista com os numeros que sao multiplos de n. list,int->list'''
    multiplos = []
    proximo = 0
    while proximo<len(lista):
        if lista[proximo]% n == 0:
            multiplos = multiplos + [lista[proximo],]
        proximo = proximo + 1
    return multiplos