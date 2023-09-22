def soma_h(N):
    '''Calcula e retorna o valor H com N termos
    entrada:int
    saída:float
    '''
    soma=0
    for numero in range(1,N+1):
        soma=soma+(1/numero)
    soma=round(soma,2)
    return soma