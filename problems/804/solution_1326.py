def filtra_pares(tupla4):
    '''Função que recebe uma tupla com 4 elementos e retorna uma nova tumpla somente com 
    oe elementos pares na mesma ordem'''
    
    result = ()
    
    if tupla4[0]%2 == 0:
        result = (tupla4[0],)
        
    if tupla4[1]%2 == 0:
        result = result + (tupla4[1],)
        
    if tupla4[2]%2 == 0:
        result = result + (tupla4[2],)
    
    if tupla4[3]%2 == 0:
        result = result + (tupla4[3],)
    
    return result