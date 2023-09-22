def soma_h(N):
    
    '''função retorna somatório de frações com
    N termos onde cada denominador é uma PA crescente de r = 1.
    int--> float'''
    
    H = [1]  
    for numero in range(2, N+1):
        H.append((numero)**-1)  
        sigma = sum(H)
    return round(sigma, 2)