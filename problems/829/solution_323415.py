def soma_h(n):
    ''' funcao calcula 1+somatorio de 1/n, int-->float'''
    somatorio=0
    for i in range(1,n+1):
        somatorio = somatorio+ 1/i
    return round(somatorio,2)