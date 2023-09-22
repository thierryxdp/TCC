def melhor_volta(matriz):
    temposMin = []
    for linha in matriz:
        tMin = min(linha)
        list.append(temposMin,tMin)
    tempo = min(temposMin)
    corredor = list.index(temposMin,tempo) + 1
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
             if tempo == matriz[linha][coluna]:
                    	     volta = coluna
	return (corredor,tempo,volta)