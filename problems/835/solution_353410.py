def melhor_volta(matriz):
    '''função que recebe como entrada uma matriz 6*10 com os tempos em segundos dos
    corredores em cada volta e retorna uma tupla informando de quem foi a melhor volta da prova,
    com qual tempo e em que volta
    list---->tuple'''
    menor_tempo = volta = vencedor = 1000
    for v in range(0, len(matriz)):
        for t in range(0, len(matriz[v])):
            if min(matriz[v][t], menor_tempo) == matriz[v][t]:
                menor_tempo = min(matriz[v][t], menor_tempo)
                vencedor = v + 1
                volta = t + 1
    return vencedor, menor_tempo, volta