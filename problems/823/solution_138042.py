def faltante(lista):
    ''' Essa função tem como objetivo identificar a peça faltante em um
    quebra cabeça, dado uma lista com as numerações das peças.'''
    '''list -> int'''
    
    falta = len(lista)+1
    N = 1
    i = 0
    while i <= falta:
        if N == falta:
            return N
        
        elif N != lista[i]:
            return N
        N= N+1
        i = i+1