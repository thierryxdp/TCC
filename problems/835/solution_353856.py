def melhor_volta(matriz):
    """Função quue recebe como entrada uma matriz 6x10 com os tempos em segundos dos corredores em cada volta,
    Dado que a pista permite 10 voltas para cada segundo, o retorno é uma tupla com 
    quem foi a melhor volta, com qual tempo e em qual volta
    list -> tuple"""
    tempo = volta = vencedor = 1000
    for v in range(0, len(matriz)):
        for t in range(0, len(matriz[v])):
            if min(matriz[v][t], tempo) == matriz[v][t]:
                tempo = min(matriz[v][t], tempo)
                vencedor = v + 1
                volta = t + 1

    return vencedor, tempo, volta