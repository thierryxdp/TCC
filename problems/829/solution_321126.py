def soma_h(n):
    '''A função retornará a soma das divisões de por (n) termos
    Dados de entrada -> int
    Dados de saída -> float'''
    
    soma = 1
    
    for i in list(range(1,n)):
        soma += + (1/(i+1))
        
    return round(soma,2)