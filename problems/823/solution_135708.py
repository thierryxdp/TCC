def faltante(lista):
    '''retorna o numero faltante na lista'''
    '''list -> int'''
    
    i=0
    soma=lista[i]+1
    
    while i < len(lista):
        if lista[i]!=soma:
            return soma