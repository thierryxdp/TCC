def soma_h(n):
    
    """
    int--->float
    para cada valor i de 1 até n, se faz a divisao de 1 por i a cada 
    leitura, os somando até que chegue ao 1/n. 
    """
    
    soma=0
    
    for i in range(1,n+1):
        soma+=1/i
        
    return round(soma,2)