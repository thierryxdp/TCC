def filtraMultiplos(lista,n):
    ''' funcao que dada uma tupla não vazia de inteiros, retorna uma tupla com os
    inteiros pares da tupla original, mantida a ordem.
    tuple --> tuple'''
    lista = ()
    proximo = 0
    while :
        if lista[proximo]%n == 0:
            lista = lista + (lista[proximo],)
        proximo = proximo + 1
    return lista