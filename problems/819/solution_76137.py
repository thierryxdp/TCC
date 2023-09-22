def filtraMultiplos(lista,n):
    '''funçao que dada uma lista com numeros inteiros,retorna apenas os multiplos de um dado numero n
    entradas: list,int
    saida: list'''
    multiplos = []
    proximo = 0
    while proximo <len(lista):
        if lista[proximo]%n == 0:
            multiplos = multiplos + [lista[proximo],]
        proximo = proximo + 1
    return multiplos