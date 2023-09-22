def faltante(lista):
    '''retorna o numero faltante na lista dada'''
    '''list -> int'''
    
    i=0
    faltante=0
    
    while i< len(lista):
        faltante = faltante + lista[i]
        i = i +1
        
        return faltante