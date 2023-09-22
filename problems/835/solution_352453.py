def melhor_volta(matriz):
    '''função que recebe como entrada uma matriz 6 x 10 com os tempos em segundos dos corredores em cada volta.A função retorna uma tupla informando (de quem foi a melhor volta da prova, com qual tempo e em que volta); list (mat) -> tuple''' 
    tempo=100000
    tup=(0,tempo)
    for i in range(6):
        for j in range(10):
            if matriz[i][j]<tup[1]:
                tup=(i+1,matriz[i][j],j+1)
    return tup