def posLetra(frase,l,n):
    '''...'''
    
    indice=1
    pos=0
    
    while indice<len(frase):
        pos = str.find(frase,l,0,5)
        indice+=1 
    return pos