def total(l=[],d={}):
    '''
    
    '''
    
    cont=0.0
    for caractere in l:
        cont+=d[caractere]
    return round(cont,2)