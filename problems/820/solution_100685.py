def posLetra(frase,l,n):
    '''...'''
    
    indice=1
    pos=0
    
    while indice<len(frase):
        pos = str.find(frase,l,n,-7)
        
        indice=indice+1        
    return pos