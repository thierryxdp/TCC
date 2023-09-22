def melhor_volta(matriz):
    temposMin = []
    for linha in matriz:
        tMin = min(linha)
        temposMin.append(tMin)
    tempo = min(temposMin)
    corredor = temposMin.index(tempo) + 1
    volta = matriz[corredor-1][tempo]
	return (corredor,tempo,volta)