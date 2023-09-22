def melhor_volta(matriz):
    """funcao que retorna o corredor que teve a volta mais rapida, o tempo
    da volta e o numero da volta;lista->tupla"""
    tempo=(1,matriz[0][0],1)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]<tempo[1]:
                tempo=(i+1,matriz[i][j],j+1)
    return tempo