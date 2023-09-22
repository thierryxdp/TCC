def soma_h(N):
    ''' Função que dado um numero inteiro, retorna a somatória
    de 1/1,1/2 até 1/N.
    Entrada: int
    Retorno: float '''
    
    soma = 0
    for x in range(1,N+1):
        soma = soma + (1/x)
    return round(soma,2)