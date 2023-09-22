def faltante(lista):
    '''
    Dada uma lista com N - 1 inteiros numerados de 1 a N, a funcao
    descobre o numero inteiro que esta faltando.
    
    Entrada/Saida:
    list -> int
    '''
    completa = range(1, max(lista) + 1)
    i = 0
    while i < len(completa) - 1:
        if completa[i] not in lista:
            return completa[i]
        i += 1
    return completa[i] + 1