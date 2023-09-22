def faltante(lista):
    tamLista = len(lista) + 1
    pecas = []
    n = 1
    total_observado = sum(lista)
    while n < tamLista:
        pecas += [(n),]
        n = n+1
    total_esperado = total_observado + n
    if lista[0] != 1:
        return 1
    else:
    	return total_esperado - total_observado