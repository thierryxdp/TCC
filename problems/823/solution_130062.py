def faltante(lista):
    '''Função que,dada uma lista, descobre qual número inteiro deste intervalo está faltando.
    lista-->int'''
	i=0
    teste = 0
    n = len(lista)
    while (i < n ) and (teste == 0):
        i = i+1
        if lista(i) == i:
            teste = 0
        else:
            faltante = i
            teste = 1
    if teste == 0 :
        faltante = n+1
    return faltante