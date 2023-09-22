def faltante(lista):
"uma função que, dada uma lista com N - 1inteiros numerados de 1 a N. retorno: int"
    pecas=len(lista)
    lista.sort()
    i=0
    while i<pecas:
    	if lista[i]!=i+1:
            return i+1
        i=i+1
    return i+1