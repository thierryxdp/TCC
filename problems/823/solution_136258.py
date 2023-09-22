def faltante(lista):
    """dada uma lista com N-1 inteiros numerados de 1 a N,retorna o número que falta.
    list->int"""
    list.sort(lista)
    i=0
    while i+1<len(lista):
        if lista[i+1]-lista[i]!=2:
        	i=i+1
    else if i+1=len(lista):
        return lista[i]-1
    return lista[i]+1