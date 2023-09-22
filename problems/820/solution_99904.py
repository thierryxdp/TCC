def posLetra(frase,l,n):
    '''...'''
    
    indice=1
    pos=0
    
    while indice<len(frase):
        if frase[l]==n:
            pos=str.find(frase,l,n)
        
        indice+=1
        
    return pos