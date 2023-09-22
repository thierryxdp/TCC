def melhor_volta(matriz):
    """Funcao que recebe como entrada uma matriz 6X10 com os tempos
    em segundos dos corredores em cada volta.
    Entrada: list, list 
    Saída: float
    """
    tupla=(0,1)
    for i in matriz(6):
        for j in matriz(10):
            if matriz[i][j]