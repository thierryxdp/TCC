def melhor_volta(matriz:list)-> tuple:
    """Função que recebe uma entrada uma matriz 6x10 com os tempos em segundos dos corredores em cada volta da corrida, e retorna uma tupla informando de quem foi a melhor volta, com qual tempo e em que volta. Onde os corredores possuem tempos diferentes."""
    melhor = 0
    volta = 0
    lista = []
    for i in range (len(matriz)):
        for j in range (len(matriz[0])):
            lista = lista + matriz [i][j]
            if matriz[i][j] == min(lista):
                melhor = i + 1
        	    volta = j + 1
    return (melhor, min(lista), volta)