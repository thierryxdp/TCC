def faltante(lista):
    """dada uma lista com N-1 inteiros numerados de 1 a N,retorna o número que falta.
    list->int"""
    list.sort(lista)
    i=0
    if i+1==len(lista):
    	return lista[i]-1
    elif while i+1<len(lista):
        	if lista[i+1]-lista[i]!=2:
        		i=i+1            
    return lista[i]+1