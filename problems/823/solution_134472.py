def faltante(lista):
    tamLista = len(lista) + 1
    n = 1
    pecas = [n]
    total_observado = sum(lista)
    while n < tamLista:
        pecas += [(n+1),]
        n = n+1
    total_esperado = total_observado + (n-1)
    if lista[0] != 1:
        return 1
    else:
    	return total_esperado - total_observado