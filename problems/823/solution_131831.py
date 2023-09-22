def faltante(lista):
    '''Função que,dada uma lista, descobre qual número inteiro deste intervalo está faltando.
    lista-->int'''
    i = 1
    faltante = ''
    if lista[0]!= 1 :
            faltante = 1
    while i<len(lista):
        if (lista[i-1]-lista[i]) != -1:
            faltante = lista[i]-1
        i = i+1
        if lista[i] == len(lista):
    	    faltante = lista[i]+1
    return faltante