def faltante(lista):
    '''retorna o numero faltante na lista dada'''
    '''list -> int'''
    
    i=0
    recip=0
    
    while i< len(lista):
        if lista[i] not in '1,2,3,4,5,6,7,8,9':
            recip=recip+lista[i]
            i=i+1
      
    return recip