def soma_h(N):
    '''Calcula e retorna o valor H resultante de uma série 
       com N termos, sendo N dado como entrada;
       int -> float'''
    
    H = 1
    
    for num in range(2,N+1):
        
        H += 1/num
        
    return round(H,2)