def faltante (lista1):
    '''Retorna qual peça está faltando entre as indicadas na lista, lista->int'''
    n = len(lista1)
    lista2 = [n+1]
    i = 1
    j = 1
    while i<n:
        lista2 = lista2 + [i]
    	i = i + 1
    while j>n:
        if lista1[j] not in lista1:
            peca = j
    return j