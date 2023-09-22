def soma_h(n):
    '''funçao que calcula o valor de h'''
    h = 0
    for c in range(0,n):
        h = 1+1/c
        h += h
    return h