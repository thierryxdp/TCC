def soma_h(n):
    '''Retorna a soma da série 1/x de x=1 até x=n;
    int -> float'''
    
    soma = 0
    
    for x in range(1, n+1):
        soma += 1/x
    
    return round(soma, 2)