def posLetra(frase,l,n):
    '''...'''
    
    indice = 1
    pos = 0
    
    while indice<=len(frase):
        pos = str.index(frase,l,n)
       
        indice+=1
        
    return pos