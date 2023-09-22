def melhor_volta(matriz):
    menor_tempo_geral = matriz[0][0]
    melhor_corredor = ''
    melhor_volta = ''
    for corredor in enumerate(matriz):
        menor_tempo_corredor = min(corredor[1])
        numero_do_corredor = corredor[0]
        volta = corredor[1].index(menor_tempo_corredor)
        if menor_tempo_corredor <= menor_tempo_geral:
            menor_tempo_geral = menor_tempo_corredor
            melhor_corredor = numero_do_corredor
            melhor_volta = volta
    return melhor_corredor, menor_tempo_geral, melhor_volta