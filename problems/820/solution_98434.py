def posLetra(frase,letra,n):
    '''...'''
    posicao = frase.find(letra)
    
    while posicao >= 0 and n > 1:
        posicao = frase.find(letra,posicao+1)
        
        n-=1
    return posicao