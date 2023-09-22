def melhor_volta(x):
    """
    funcao que recebe uma matriz 6x10 com os tempos em segundos dos corredores em cada volta. a funcao deve retornar uma tupla informando quem
    teve a melhor volta, com qual tempo e em que volta.
    list -> tuple
    """
    temp = volta = venc = 1000
    for v in range(0, len(x)):
        for t in range(0, len(x[v])):
            if min(x[v][t], temp) == x[v][t]:
                temp = min(x[v][t], temp)
                venc = v + 1
                volta = t + 1