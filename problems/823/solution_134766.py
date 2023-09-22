def faltante(lista):
    '''...'''
    
    
    indice = 1
    n = max(1,2,3,4,5,6,7,8,9)
    while indice<len(lista):
        str.sort(n)
        if lista[indice]==n:
                n = sum(lista)-1
          
        indice+=1
        
    return n