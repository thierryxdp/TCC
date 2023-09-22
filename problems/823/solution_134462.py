def faltante(lista):
    tamLista = len(lista) + 1
    pecas = []
    n = 1
    total_observado = sum(lista)
    while n < tamLista:
        pecas += [(n + 1),]
        n = n+1
    total_esperado = total_observado + n
    if lista[i] != 1:
        return 1
    else:
    	return total_esperado - total_observado