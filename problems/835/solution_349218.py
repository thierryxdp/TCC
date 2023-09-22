def melhor_volta(matriz):
    """funcao que recebe como entrada uma matriz 6x10, a funcao retorna uma tupla
    informando de quem foi a melhor volta da prova. list->tupla."""
    menor_elemento=(matriz[0][0],matriz[0][0])
    for i in range(0,6,1):
        for j in range(0,10,1):
            if matriz[i][j]<menor_elemento[1]:
                menor_elemento=(i+1,matriz[i][j],j+1)
                
    return menor_elemento