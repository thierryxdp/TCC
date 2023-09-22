def melhor_volta(matriz):
    menor_tempo = volta = vencedor = 1000
    for v in range(0, len(matriz)):
        if min(matriz[v][t], menor_tempo) == matriz[v][t]:
            menor_tempo = min(matriz[v][t], menor_tempo)
            vencedor = v + 1
            volta = t + 1
            
    return vencedor, menor_tempo, volta