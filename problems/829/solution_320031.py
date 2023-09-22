def soma_h(n):
    '''Função que tem o objetivo de calcular e retornar o valor H com N termos, onde n é o número inteiro recebido como entrada.
    int->float.'''
    soma = 0
    for h in range(1,n+1):
        soma += (1/(h))
    return round(soma,2)