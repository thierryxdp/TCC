def faltante(l):
    """Recebe uma lista "l" de tamanho N-1 contendo inteiros não repetidos de 1 a N e retorna o inteiro x que pertence ao intervalo [1,N] que não está na lista de entrada "l";list->int"""
    l=l.sort()
    i=0
    while i<len(l)+1:
        if i+1 not in l:
            return i+1
        if l[i]!=i+1:
            return i+1
        else:
            i=i+1
    return i