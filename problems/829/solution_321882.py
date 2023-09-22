def soma_h (n):
    '''Dado um numero inteiro n retorna a soma 
    de 1 + 1/2 + 1/2 + 1/3 + 1/4 +...+ 1/n;
    int-> float'''
    soma=0
    for x in  range(1,n+1):
        soma= soma + x**(-1)
    return round(soma,2)