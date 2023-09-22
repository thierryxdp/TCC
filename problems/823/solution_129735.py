def faltante(L):
    '''retorna o numero inteiro que pertence ao intervalo de N elementos mas nao pertence a lista de entrada
    tupla -> int'''
    t=len(L)+1
    L.sort()
    a=0
    while a<t:
        if a+1 not in L:
            return a+1
        if L[a] != a+1:
            return a+1
        else:
            a += 1