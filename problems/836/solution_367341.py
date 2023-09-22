def busca(setor,matriz):
    dados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if setor in matriz[i]:
                matriz[i].remove(setor)
                dados.append(matriz[i])
	return dados