def soma_h(N):
    """função que calcula o resultado do somatório de 1 até 1/N
    int->float"""
    soma=1
    for numero in range(1,N):
        soma=soma+(1/numero)
    return round(soma,2)