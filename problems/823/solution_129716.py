def faltante(L):
    """Pede uma lista com N-1 inteiros (sem repetição)
    que podem variar de 1 até N.
    Retorna o número que está faltando no intervalo [1,N].
    list->int"""
    i = 0
    L.sort()
    L.append(L[len(L)-1]+1)
    while i < len(L):
        if L[i]!=i+1:
            return i+1
        i = i + 1
    return i