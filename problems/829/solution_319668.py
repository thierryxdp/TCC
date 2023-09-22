def soma_h(n):
    """Função que calcula o valor de hm com n termos.
        int->float"""
    soma=0
    for i in range(n+1):
        soma=soma+1/i
        round(soma,2)
    return soma