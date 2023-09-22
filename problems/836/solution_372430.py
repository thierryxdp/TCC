def busca(setor,matriz):
    resultado = []
    i = 0
    for linha in matriz:
        for coluna in linha:
            i +=1
            if coluna == setor:
                resultado.append(matriz[i][0])
                resultado.append(matriz[i][1])
                resultado.append(matriz[i][3])
                
	return resultado