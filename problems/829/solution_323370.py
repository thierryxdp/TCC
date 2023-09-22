def soma_h(N):
    """
    retorna a soma em questão dado o N
    """
    
    H=0
    
    for x in range(N):
        H+=1/(x+1)
        
    return round(H,2)