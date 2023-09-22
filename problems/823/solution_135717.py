def faltante(lista):
    '''retorna o numero faltante na lista'''
    '''list -> int'''
    i=0
    soma=i+1
    pa=[]
    
    while i < len(lista):
        if lista[i] != soma:
            pa=soma
            i=i+1
        else:
            return soma