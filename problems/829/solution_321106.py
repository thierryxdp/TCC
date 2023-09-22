def soma_h(N):
    '''Função que dado um número inteiro (N) retorna o somatório
    1 + 1/ por cada número a partir do 2 até chegar no N.
    int -> float'''
    
    somatorio=1
    
    for i in range(2,N+1):
        somatorio=somatorio+1/i
         
    return round(somatorio,2)