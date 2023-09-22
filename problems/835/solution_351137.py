def melhor_volta(matriz):
    """retorna de quem foi a melhor volta, o tempo e qual volta (lista-> tupla)"""
    tupla = (1,float('inf'),1)
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < tupla[1]:
                tupla = (i+1,matriz[i][j],j+1)

    return tupla