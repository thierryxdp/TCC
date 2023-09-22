def melhor_volta (matriz):
    melhor = [-1,999999, -1] #Lista com o melhor resultados
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if matriz[i][j] < melhor[1]:
                melhor[0] = i # Número do corredor
                melhor[1] = matriz[i][j] # Tempo
                melhor[2] = j # Número da volta
    return tuple(melhor)