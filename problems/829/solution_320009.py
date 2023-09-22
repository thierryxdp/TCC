def soma_h(n):
    """calculo e retorno de uma funçao que retorne o valor H com N termos."""
    soma=0
    for i in range(1,n+1):
        soma+=1/i
    return round(soma,2)