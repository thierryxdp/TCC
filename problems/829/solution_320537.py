def soma_h(N):
    '''A função recebe um número inteiro N e retorna o valor de H com N termos, dado
    a equação, com somente 2 casas decimais.
    Parâmetro de entrada: int
    Valor de retorno: float'''
    soma=0
    for numero in range(1,N+1):
        soma=soma+1/numero
    return round(soma,2)