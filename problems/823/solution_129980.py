def faltante(lista):
    '''Função que,dada uma lista, descobre qual número inteiro deste intervalo está faltando.
    lista-->int'''
    i = 0
    faltante = ''
    while i<len(lista):
        if (lista[i-1]-lista[i]) != -1:
            faltante = lista[i]-1
        if lista[0]!= 1 :
            faltante = 1
        i = i+1
   	return faltante