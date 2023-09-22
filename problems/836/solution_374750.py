def busca(buscar,matriz):
    lista = []
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if buscar == matriz[l][c]:
                del(matriz[l][c])
                lista.append (matriz[l])
	return lista