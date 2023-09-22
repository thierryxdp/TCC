def filtraMultiplos(t,n):
    '''Dada uma lista não vazia de inteiros e um número inteiro, 
    retorna uma lista com os inteiros multiplos do número dado.
    list --> list'''
    lista = []
    proximo = 0
    while proximo <len(t):
        if t[proximo]%n == 0:
            lista = lista + [t[proximo],]
        proximo = proximo + 1
    return lista