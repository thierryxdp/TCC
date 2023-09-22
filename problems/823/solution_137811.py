def faltante (lista):
    '''dada uma lista de números de quantidade n-1, retorna o valor que falta para completar n números
    list->int'''
    
    i=0
    
    while i <len (lista):
        if i < (len (lista))-1:
        	if lista[i]+1 != lista [i+1]:
            	return lista[i]+1
        if lista [0] != 1:
            return 1
        if i == len (lista)-1:
            return lista[len(lista)-1] +1
        i=i+1