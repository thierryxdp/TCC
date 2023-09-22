def faltante(lista):
    '''Funçao que retorna o numero inteiro que falta
    em uma lista numerada de 1 a N. list -> int'''
    
    
    i = 0
    
    while i<len(lista):
        if L[i]!=i+1:
            return i+1
        i=i+1
    return i+1