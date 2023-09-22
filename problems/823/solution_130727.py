def faltante(pecas):
    '''Dada uma lista de numeros naturais
    consecutivos, exceto o 0, com um elemento
    faltando na lista, a funcao retorna esse
    elemento faltoso.
    list -> int'''
    pecas.sort()
    i=0
    while pecas[i]==i+1:
        i=i+1
	return i+1