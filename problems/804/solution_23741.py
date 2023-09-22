def filtra_pares(x):
    '''cria uma lista vazia, filtra os elementos dados
	em  pares e não pares, retorna os pares numa tupla
    ordenada'''
    y = []
    for z in x:
        while z%2==0:
            y.append(z)
            return (tuple(y))