def qtd_divisores(n):
    """ Conta quantos divisores o número n possui"""
    x = 0 
    for i in range(1,n//2 + 1):
        if n%i == 0:
            x = x + 1
    if n==0 or n<0:
        return 0
    else:
        return x + 1