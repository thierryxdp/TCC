def melhor_volta(matriz):
    temposMin = []
    for linha in matriz:
        tMin = min(linha)
        list.append(temposMin,tMin)
    tempo = min(temposMin)
    corredor = temposMin.index(tempo) + 1
    for linha in matriz:
        for coluna in linha:
    volta = matriz[corredor-1][matriz[corredor-1].index(tempo)]
	return (corredor,tempo,volta)