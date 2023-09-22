def melhor_volta(matriz):
    """essa função recebe uma matriz contendo o tempo 
    dos corredores de uma corrida de kart e retorna 
    uma tupla mostrando quem fez a melhor volta, 
    juntamente com o tempo e o número da volta;
    list->tuple"""
    tupla = (0,float('inf'),0)
    for i in range (6):
        for j in range(10):
            if matriz[i][j] < tupla[1]:
                tupla = (i + 1, matriz[i][j], j + 1)
    return tupla