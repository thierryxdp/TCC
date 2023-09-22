def peça_perdida(lista):
    '''Função que,dada uma lista, descobre qual número inteiro deste intervalo está faltando.
    lista-->int'''
    i = 0
    peça_perdida = ''
    while i<len(lista):
        if (lista[i-1]-lista[i]) != -1:
            peça_perdida = lista[i]-1
        if lista[0]!= 1 :
            peça_perdida = 1
        i = i+1
    return peça_perdida