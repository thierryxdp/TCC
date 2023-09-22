def posLetra(frase,l,n):
    '''...'''
    
    indice = 0
    posicao = 1
    
    while indice<len(frase):
        posicao = str.find(frase,l,n)
        indice+=1
        
    return posicao