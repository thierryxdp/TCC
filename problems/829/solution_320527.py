def soma_h(n):
    '''funçao que calcula o valor de h'''
    x = 0
    h = 0
    for c in range(1,n+1):
        h = 1/c
        x += h
    return round(x,2)