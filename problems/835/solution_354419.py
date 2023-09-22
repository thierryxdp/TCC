def melhor_volta(matriz):
    temposMin = []
    for linha in matriz:
        tMin = min(linha)
        list.append(temposMin,tMin)
    tempo = min(temposMin)
    corredor = list.index(temposMin,tempo) + 1
    for linha in matriz:
        for coluna in linha:
            	if tempo == matriz[linha][coluna]:
                    volta = coluna
	return (corredor,tempo,volta)