def filtraMultiplos(lista, n):
    ''' funcao que dada uma lista não vazia de inteiros, retorna uma lista com os
    inteiros divisiveis por n.
    list --> list'''
    multiplos = []
    proximo = 0
    while proximo <len(lista):
        if lista[proximo]%n == 0:
            multiplos = multiplos + [lista[proximo]]
        proximo = proximo + 1
    return multiplos