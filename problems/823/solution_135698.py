def faltante(lista):
    '''retorna o numero faltante na lista'''
    '''list -> int'''
    
    i=0
    soma=0
    
    while i < len(lista):
        if soma not in lista:
            soma=soma+lista[i]
            i=i+1
            
        return soma