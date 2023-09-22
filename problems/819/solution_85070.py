def filtra_multiplos(lista):
    ''' funcao que dada uma tupla não vazia de inteiros, retorna uma tupla com os
    inteiros pares da tupla original, mantida a ordem.
    list --> list'''
    multiplos = []
    proximo = 0
    while proximo <len(lista):
        if lista[proximo]%n == 0:
            multiplos = multiplos + [lista[proximo]]
        proximo = proximo + 1
    return multiplos