def faltante(lista):
    '''Retorna o número faltante na lista de inteiros dada; list[int] -> int'''
    list.sort(lista)
    if lista[0]!=1:
        return 1
    indice=1
    while indice<len(lista):
        if lista[indice]!=lista[indice-1]+1:
            return lista[indice-1]+1
        indice=indice+1
	return lista[indice-1]+1