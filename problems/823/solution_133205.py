def faltante(lista):
    '''A partir da lista de entrada indicando as pecas que
    presentes, a funcao retorna qual o numero da peca que
    esta faltando.
    list -> int'''
    k = 0
    lista = list.sort(lista)
    list.append(lista,0)
    while (k+1) == lista[k]:
        k += 1
	return k+1