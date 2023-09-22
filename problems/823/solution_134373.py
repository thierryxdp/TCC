def faltante (L):
    """Retorna um número inteiro que pertence ao intervalo [1,N], mas que não 
    pertence à lista de entrada L. list-> int"""
    i = L[0]
    a = 0
    if L[0] == 1:
        while (i == L[a]):
            if a < len(L):
                i = i + 1
                a = a + 1
            else:
                i = 1
        return i
    else:
        return L[-1] + 1