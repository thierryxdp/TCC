def soma_h(N):
    '''
    	funcao que recebe N para calcular e retornar o valor H com N termos.
        N:int
        H:int
        return:float
    '''
    H = 0
    for i in range(1, N+1):
        H = H+1/i
    return round(H,2)