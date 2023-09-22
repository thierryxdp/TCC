def faltante(L):
    '''função que retorna o valor faltante 
    numa lista:
    valor de entrada: list
    valor de saída: int'''
    L=L.sort()
    n=max(L)
    while n > len(L):
        if n not in L:
            return n
        n=n-1