def filtraMultiplos(lista,n):
    ''' funcao que dada uma tupla não vazia de inteiros, retorna uma tupla com os
    inteiros pares da tupla original, mantida a ordem.
    tuple --> tuple'''
    lista2 = []
    proximo = 0
    while proximo <len(lista):
        if lista[proximo]%n == 0:
            lista2 = lista[proximo]
            lista2.append=[lista2]
        proximo = proximo + 1
    return lista2