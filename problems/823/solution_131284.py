def faltante(lista):
    ''' Funcao que dada uma lista com numero de pecas de um quebra cabeca (faltando uma peca), retorna o numero da peca faltante.
    list -> int'''
    
    i = 0
    listaCompleta = range(1, max(lista) + 1)
    
    while i < len(listaCompleta):
        if listaCompleta[i] not in lista:
            return listaCompleta[i]
        
    	i += 1