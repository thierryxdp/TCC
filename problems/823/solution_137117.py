def faltante(L):
    """
    recebe uma lista de números inteiros dentro de um intervalo e retorna
    o número inteiro que está no intervalo porém não está na lista.
    """
    list.sort(L)
    if L[0]!=1:
        return 1
    i=1
    while i<len(L):
        if L[i]!=L[i-1]+1:
            return L[i-1]+1
        i=i+1