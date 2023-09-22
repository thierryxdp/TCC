def melhor_volta(matriz):
    """função que recebe uma matriz 6 x 10 com os tempos em segundos dos corredores
    em cada volta e retorna uma tupla informando: De quem foi a melhor volta da prova,
    com qual tempo e em que volta.
    list -> tuple"""
    volta = matriz[0][0]
    indice = 1
    corredor = 1
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if volta > matriz[i][j]:
                volta = min(volta, matriz[i][j])
            	indice = j + 1
                corredor = i + 1
	return corredor, volta, indice