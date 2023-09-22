def melhor_volta(matriz):
    """Dada uma matriz 6 x 10 e o tempo dos 6 corredores em cada volta de uma
    pista de kart que permite 10 voltas, retorna de quem foi a melhor volta
    da prova, com qual tempo e em que volta."""
    tempo = volta = vencedor = 1000
    for v in range(0, len(matriz)):
        for t in range(0, len(matriz[v])):
            if min(matriz[v][t], tempo) == matriz[v][t]:
                tempo = min(matriz[v][t], tempo)
                vencedor = v + 1
                volta = t + 1

    return vencedor, tempo, volta