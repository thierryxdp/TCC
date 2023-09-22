def soma_h(N):
    '''Função que calcula a soma H com N termos
    int -> float'''
    
    soma = 0
    
    for m in list(range(1, N+1)):
        parcial = 1 / m
        
        soma = soma + parcial
        
    return round(soma, 2)