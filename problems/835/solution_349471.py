import math
def melhor_volta(tempos):
    """Função que recebe como entrada uma matriz 6 x 10 com os tempos em segundos e retornar uma tupla com a melhor volta,
    matriz --> tupla"""
    t = (0,math.inf,0)
    for i in range(6):
        for j in range(10):
            if tempos[i][j] < t[1]:
                 t = (i+1,tempos[i][j],j+1) 
    return t