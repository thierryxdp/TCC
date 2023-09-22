def faltante (lista):
    '''Funcao que, dada uma lista N-1, retorna o numero inteiro que está falatando.
    list->int'''
    
    i=0
    pecas=0
    list.sort(lista)
    
    while i != (len(lista)-1):
        if pecas == lista[i]:
            i=i+1
            pecas=pecas+1
         
        elif pecas == lista[-1]:
            return pecas+1
        
        else:
            return pecas