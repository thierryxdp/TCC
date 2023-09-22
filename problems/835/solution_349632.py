import math

def melhor_volta(matriz):
    melhor_corredor = 0
    menor_tempo = math.inf
    saida = ()
    for i in range(len(matriz)):
        menor_tempo_volta = min(matriz[i])
        if menor_tempo_volta < menor_tempo:
            saida = (matriz[i].index(menor_tempo_volta)+1, menor_tempo_volta, i+1)
            menor_tempo = menor_tempo_volta
    return saida