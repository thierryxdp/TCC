def melhor_volta(matriz):
    """
    função que recebe como entrada uma matriz 6x10 com os tempos(em segundos) dos 
    corredores em cada volta. A função possui como retorno uma tupla informando de
    quem foi a melhor volta, o tempo e em que volta ocorreu.
    list -> tuple
    """
    tempo = volta = vencedor = 1000
    for x in range(0, len(matriz)):
        for t in range(0, len(matriz[x])):
            if min(matriz[x][t], tempo) == matriz[x][t]:
                tempo = min(matriz[x][t], tempo)
                vencedor = x + 1
                volta = t + 1

    return vencedor, tempo, volta