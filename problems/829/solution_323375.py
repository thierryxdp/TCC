def soma_h(N):
    '''
    função que calcula o valor de H de acordo com a expressão dada.
    '''
    numero=1
    soma=0
    for numero in range(1,N+1):
        soma = soma+(numero/N)
    return round(soma,2)