def soma_h(N):
    """Calcula e retorna o valor da soma H, com N termos;int->float"""
    soma=0
    for i in range(N):
        soma=soma+(1/N)
    return round(soma,2)