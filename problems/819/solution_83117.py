def filtraMultiplos(t:list,n):
    ''' funcao que dado uma lista não vazia de inteiros,
    retorna uma lista com os inteiros multiplos da lista
    original, mantida a ordem. str -> str'''
    pares = []
    proximo = 0
    while proximo <len(t):
        if t[proximo]%n == 0:
            pares = pares + [t[proximo],]
        proximo = proximo + 1
    return pares