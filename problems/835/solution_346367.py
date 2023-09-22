def melhor_volta(matriz_tempos):
    """calculo e retorno de uma funçao que retorna a melhor volta, o tempo e qual volta."""
    volta = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if matriz_tempos[i][j] < volta[1]:
                volta = (i+1,matriz_tempos[i][j],j+1) #de quem, tempo, qual volta
    return volta