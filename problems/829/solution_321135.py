def soma_h(N):
    """calcula e retorna o valor H com N termos, o resultado é dado com 2 casas decimais.
    int->float"""
    soma=0
    for n in range(1,N+1):
        soma=soma+(1/n)
    return round(soma,2)