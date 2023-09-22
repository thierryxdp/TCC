def faltante(lista):
    '''...'''
    
    
    indice = 1
    n = [1:9]
    while indice<len(lista):
        if (lista[indice])==n:
             n+=(n-1)
          
        
        indice+=1
        
    return n