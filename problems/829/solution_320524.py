def soma_h(n):
    '''funçao que calcula o valor de h'''
    h = 0
    for c in range(1,n+1):
        h = 1/c
        h += h
    return round(h,2)