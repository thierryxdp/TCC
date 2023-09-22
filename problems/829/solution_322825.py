def soma_h(N):
    
    ''' Função que calcula o valor H com N termos, tal 
        que N é inteiro e dado como entrada.
        int -> float '''
    
    H = 0 
    
    for numero in range(1,N+1):
        H += 1/numero
        
    
    return round(H, 2)