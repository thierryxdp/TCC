def faltante(lista):
    '''Função que,dada uma lista, descobre qual número inteiro deste intervalo está faltando.
    lista-->int'''
	i=1
    teste = True
	while (i<=len(lista)) and ((teste) = True):
        if lista[i] = i:
            teste = True
        	i = i+1
        else:
            faltante = lista[i]
            teste = False
    if teste = True :
        faltante = i+1
    return faltante