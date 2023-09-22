def soma_h(N):
    """Calcula e retorna o valor da soma H, com N termos;int->float"""
    soma=0
    for i in range(1,N+1):
        soma=soma+(1/i)
    return round(soma,2)