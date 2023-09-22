def filtraMultiplos(lista,numero):
    '''Função que, dada uma lista com numeros inteiros,
    filtre os multiplos de um numero n
    list, int -> list'''
    i = 0
    n = []
    while i<len(lista):
        if lista[i]%numero==0:
            n = n + [lista[i]]
        i = i + 1
    return n