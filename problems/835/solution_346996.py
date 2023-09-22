from math import inf
def melhor_volta(matriz6x10):
    """
    list -> tuple
    """
    quem  = 0   #quem teve a melhor volta
    tempo = inf #qual o tempo da volta
    volta = 0   #em que volta

    for i in range(len(matriz6x10)):
        for j in range(len(matriz6x10[0])):
            if matriz6x10[i][j] < tempo:
                tempo = matriz6x10[i][j]
                quem = i
                volta = j

    return quem,tempo,volta