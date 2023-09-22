def soma_h(N):
    """funçao que retorna a soma de uma serie; int->float"""
    soma=0
    for termo in range(N):
        soma+=1/(termo+1)
    return round(soma,2)