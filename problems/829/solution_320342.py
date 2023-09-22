def soma_h(N):
    '''retorna a soma dos inversos de 1 até n''' 
    soma=0
    for i in range(1,N+1):
        soma+=1/i
    return round(soma,2)