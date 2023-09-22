def melhor_volta(matriz):
    """Função que receba como entrada uma matriz 
    6 x 10 com os tempos em segundos dos corredores 
    em cada volta;
    list -> tuple"""
    

menorTempo = volta = vencedor = 1000
for v in range(0, len(matriz)):
    for t in range(0, len(matriz[v])):
        if min(matriz[v][t], menor_tempo) == matriz[v][t]:
            menorTempo = min(matriz[v][t], menor_tempo)
            vencedor = v + 1
            volta = t + 1

return vencedor, menorTempo, volta