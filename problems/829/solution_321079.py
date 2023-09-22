def soma_h(N):
    '''retorna a soma dos inversos de 1 até n'''
    return round(sum(map(lambda x:1/x, range(1,N+1))),2)