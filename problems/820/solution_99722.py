def posLetra(frase,l,n):
    '''...'''
    
    indice = 1
    posicao = 0
    
    while indice<len(frase):
        posicao = str.count(frase,l,n)
        indice+=1
        
    return posicao