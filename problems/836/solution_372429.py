def busca(setor,matriz):
    resultado = []
    i = 0
    for linha in matriz:
        for coluna in linha:
            if coluna == setor:
                resultado.append(matriz[i][0])
                resultado.append(matriz[i][1])
                resultado.append(matriz[i][3])
                i +=1
	return resultado