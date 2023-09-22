def melhor_volta(matriz):
    """função que recebe uma matriz 6 x 10 com os tempos em segundos dos corredores
    em cada volta e retorna uma tupla informando: De quem foi a melhor volta da prova,
    com qual tempo e em que volta.
    list -> tuple"""
    volta = matriz[0][0]
    indice = 0
    corredor = 0
    for i in range(len(matriz)):
        for j in range(matriz[i]):
            if volta > matriz[i][j]:
                volta = min(volta, matriz[i][j])
            	indice = j
                corredor = i
	return corredor, volta, indice