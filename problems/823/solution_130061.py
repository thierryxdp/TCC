def faltante(lista):
    '''Função que,dada uma lista, descobre qual número inteiro deste intervalo está faltando.
    lista-->int'''
	i=1
    teste = 0
    n = len(lista)
    while (i < n ) and (teste == 0):
        if lista[i] == i:
            teste = 0
        i = i+1
        else:
            faltante = lista[i]
            teste = 1
    if teste == 0 :
        faltante = n+1
    return faltante