def melhor_volta(matriz):
    '''função que receba como entrada uma matriz 6 x 10 com os tempos em segundos dos corredores em
    cada volta. A função deve retornar uma tupla informando: de quem foi a melhor volta da prova, 
    com qual tempo e em que volta;
    mat -> tupl'''
    temposMin = []
    for linha in matriz:
        tMin = min(linha)
        list.append(temposMin,tMin)
    tempo = min(temposMin)
    corredor = list.index(temposMin,tempo) + 1
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
             if tempo == matriz[linha][coluna]:
                    	     volta = coluna + 1
	return (corredor,tempo,volta)