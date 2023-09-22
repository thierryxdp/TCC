def faltante (L):
    """Retorna um número inteiro que pertence ao intervalo [1,N], mas que não 
    pertence à lista de entrada L. list-> int"""
    i = L[0]
    a = 0
    if L[0] == 1:
        while (a < len(L))and (i == L[a]) :
            i = i+1
            a = a + 1
        if a >= len(L):
            i = L[-1] + 1
        return i
    else:
        return 1