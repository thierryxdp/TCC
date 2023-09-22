def soma_h(N):
    """ Funçao que calcula e retorna o valor H com N termos """
    soma = 0
    for i in range(1, N+1):
        termos = (1/i)
        soma += termos
        
    return round(soma,2)