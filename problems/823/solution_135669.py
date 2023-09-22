def faltante(lista):
    '''retorna o numero faltante na lista'''
    '''list -> int'''
    
    i=0
    soma=0
    
    while i < len(lista):
        
        soma=sum(lista)/len(lista)
        i=i+1
        
    return soma