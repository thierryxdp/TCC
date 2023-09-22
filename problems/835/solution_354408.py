def melhor_volta(matriz):
    temposMin = []
    for linha in matriz:
        tMin = min(linha)
        temposMin.append(tMin)
    melhorV = min(temposMin)
	return (melhorV)