def faltante(pecas):
    '''Dada uma lista de numeros naturais
    consecutivos, exceto o 0, com um elemento
    faltando na lista, a funcao retorna esse
    elemento faltoso.
    list -> int'''
    pecas_org=pecas.sort()
    i=0
    while pecas_org[i]==i+1:
        i=i+1
	return pecas_org