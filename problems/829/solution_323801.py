def soma_h(n):
    """
    Essa função ira retornar a soma da serie harmonica de 1/n
    int->float
    """
    
    soma = 1
    for e in range(2,n+1):
        soma += 1/e
        
    return round(soma,2)