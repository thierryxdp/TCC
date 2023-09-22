def faltante (lista):
    '''dada uma lista de números de quantidade n-1, retorna o valor que falta para completar n números
    list->int'''
    
    i=0
    
    while i <len (lista):
        if lista[i]+1 != lista [i+1]:
            return lista[i]+1
        i=i+1