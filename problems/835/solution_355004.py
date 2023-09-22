# Questão 4
def melhor_volta(matriz):
    menorTempo = volta = vencedor = 1000
    for v in range(0, len(matriz)):
        for t in range(0, len(matriz[v])):
            if min(matriz[v][t], menorTempo) == matriz[v][t]:
                menorTempo = min(matriz[v][t], menorTempo)
                vencedor = v + 1
                volta = t + 1
    return vencedor, menorTempo, volta