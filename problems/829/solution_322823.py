def soma_h(N):
    
    ''' Função que calcula o valor H com N termos, tal 
        que N é inteiro e dado como entrada.
        int -> float '''
    
    H = 1 
    
    for numero in range(1,N+1):
        H += round(1/numero, 2)
        
    
    return H