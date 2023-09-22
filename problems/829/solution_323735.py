def soma_h(N):
    '''
    Recebe um inteiro positivo N e retorna a soma da série harmônica com N termos
    
    int -> float
    '''
    S=0
    for i in range(1,N+1):
    	S+=1/i
    return S