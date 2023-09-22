def soma_h(N):
    '''
    dado um numero inteiro, retorna a soma "1 + 1/2 + 1/3
    + ... + 1/N" com aproximacao de duas casas decimais
    dados de entrada: int
    retorna: float
    '''
    soma = 1
    for i in range(2,N+1):
        soma = soma + (1/i)
    return round(soma,2)