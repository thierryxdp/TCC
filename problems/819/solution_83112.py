def filtraMultiplos(listanumeros,n):
    ''' funcao que dada uma lista com numeros interios e um numero n retorna uma so com os multiplos desse numero n
    list-->list'''
    multiplos=[]
    proximo = 0
    while proximo< len(listanumeros):
        if listanumeros[proximo]%n == 0:
            multiplos = listanumeros[proximo] + multiplos[proximo]
        proximo = proximo + 1
    return multiplos