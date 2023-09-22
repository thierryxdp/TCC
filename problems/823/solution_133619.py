def faltante(lista):
    '''Retorna a peça faltante em uma sequencia crescente de numeros.
    lista --> int'''
    i = 1
    parada = False
    if len(lista) == 1:
        if lista[0] == 1:
            return 2
        else:
            return 1
    while i < len(lista) and  not parada:
        if lista[i] != (lista[i-1]+1):
            parada = True

        i += 1
	if parada:
        return i
    if lista[0] != 1:
        return 1
    else:
        return i+1