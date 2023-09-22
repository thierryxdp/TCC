def soma_h(n:int)-> float:
    '''Função chamada soma h para calcular e retornar o valor H com N termos'''
    soma=0
    for i in range(1,n+1):
        soma=soma+(1/i)
    return round(soma,2)