def faltante(pecas):
    '''Dada uma lista de numeros naturais
    consecutivos, exceto o 0, com um elemento
    faltando na lista, a funcao retorna esse
    elemento faltoso.
    list -> int'''
    pecas.sort()
    pecas.append() #adiciona um item caso a peca que esteja faltando por a ultima
    i=0
    while pecas[i]==i+1:
        i=i+1
	return i+1