def busca(buscar,matriz):
    lista = []
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if buscar == matriz[l][c]:
                lista.append(matriz[l])
    for l in range(len(lista)):
        del(lista[l][3])
	return lista