def faltante (lista):
    '''Funcao que, dada uma lista N-1, retorna o numero inteiro que está falatando.
    list->int'''
    
    i=0
    peças=0
    list.sort(lista)
    
    while i != (len(lista)-1):
        if peças == lista[i]:
            i=i+1
            peças=peças+1
         
        elif peças == lista[-1]:
            return peças+1
        
        else:
            return peças