def faltante(listaL):
    
    '''Função que dada uma lista com N peças de um quebra cabeça, identifica e retorna o número identificador da faltante. list -> int'''
    
    list.sort(listaL)
    
    i = 0
    
    while i < (len(listaL) - 1):
        if listaL[(i + 1)] != listaL[i] + 1:
            return (listaL[i] + 1)
        i = i + 1