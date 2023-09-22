def posLetra(frase,l,n):
    '''...'''
    
    indice = 1
    posicao = 0
    
    while indice<=len(frase[n]):
        posicao = str.find(frase,l,n)
        
        indice+=1
        
    return posicao