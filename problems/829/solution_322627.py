def soma_h(n):
    '''Retorna o valor h da função h(n) = 1+1/1+1/2+1/3...1/n ,
    dado a variável n, tal que n pertence aos inteiros.
    int -> float'''
    h = 1
    for div in range(1,n+1):
        h += 1/div
    return round(h,2)