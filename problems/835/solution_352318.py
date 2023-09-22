def melhor_volta(matriz):
    """
    Ao inserir uma matriz retorna quem deus a melhor volta,
    qual foi a melhor volta e em que volta aconteceu a melhor volta;
    list->tupla
    """
    resposta= [0,0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < matriz[resposta[0]][resposta[1]]:
                tempo= matriz[i][j]
                resposta=[i,j]
                piloto=i+1
                volta=j+1
    return piloto, tempo, volta