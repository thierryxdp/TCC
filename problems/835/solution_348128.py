def melhor_volta(matriz):
    """determina qual o vencedor de uma corrida e seus resultados;
    matriz, -> tupla"""
    
    x = (0,float('inf'),0)

    for i in range(6):
        for j in range(10):
            if matriz_tempos[i][j] < x[1]:
                x = (i+1,matriz_tempos[i][j],j+1)
    return x