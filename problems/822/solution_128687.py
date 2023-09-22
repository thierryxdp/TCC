def repetidos(lista):
    '''Retorna o número de vezes que um elemento da lista dada é igual ao anterior; list[int] -> int'''
    indice=1
    repeticoes=0
    while indice<len(lista):
        if lista[indice]==lista[indice-1]:
            repeticoes=repeticoes+1
        indice=indice+1
	return repeticoes