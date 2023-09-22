def maiores(ni,n):
    """ função recebe uma lista e um numero inteiro n e devolve só do N pra frente usando a função sorted e o fatiamento de listas"""
    ni.append(n)
    y = sorted(ni)
    a = y.index(n)
    return y[a+1:]