def faltante(lista):
    '''Retorna a peça faltante em uma sequencia crescente de numeros.
    lista --> int'''
    i = 1
    parada = 0
    if len(lista) == 1:
        if lista[0] == 1:
            return 2
        else:
            return 1
    while i < len(lista):
        if lista[i] != (lista[i-1]+1):
            parada = i+1
            i = len(lista)**2

        i += 1
	if i == (len(lista)**2)+1:
        return parada
    if lista[0] != 1:
        return 1
    else:
        return i+1