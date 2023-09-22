def melhor_volta(matriz):
    """ A função melhor_volta, recebe como entrada uma matriz 6 x 10 com os tempos em segundos dos corredores em cada volta e retornar uma tupla informando de quem foi a melhor volta da prova, com qual tempo e em que volta
  list-->tuple"""
    
    nlin = len(matriz)
    ncol = len(matriz[0])
    menor_tempo = 99999999
    for i in range(nlin):
        if menor_tempo>min(matriz[i]):
            menor_tempo = min(matriz[i])
    for i in range(nlin):
        for j in range(ncol):
            if matriz [i][j] == menor_tempo:
                return (i+1,menor_tempo,j+1)