def qtd_divisores(n):
    '''Funçao retorna, dado um numero n, quantos divisores ele possui'''
    quantos = 0
    for a in range(1, n+1):
        if n%a==0:
            quantos += 1
            
    return quantos