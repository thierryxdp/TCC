def faltante(lista):
    '''retorna o numero faltante na lista dada'''
    '''list -> int'''
    
    i=0
    num=1
    faltante=0
    while i <= len(lista):
        if lista[i] != num:
            faltante=lista[i]
            num=num+1
            i=i+1
            
        return faltante