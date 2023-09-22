def soma_h(N):
    '''
    	Função que recebe um número
        inteiro N e retorna a soma H 
        dada pela fórmula 
        H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N
        : param N: int
        : return: float
    '''
    H = 0
    lista = list(range(1,N+1))
    
    for numero in lista:
        H += 1/numero
    
    return round(H,2)