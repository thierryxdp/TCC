def melhor_volta (matriz: list) -> tuple:
    """Retorna uma tupla cujas posições são, respectivamente, qual corredor
    teve a melhor volta da prova, qual foi o seu tempo e em que volta."""
    melhor_volta_corredor_1 = min(matriz[0])
    volta_corredor_1 = matriz[0].index(melhor_volta_corredor_1) + 1
    melhor_performance = [1, melhor_volta_corredor_1, volta_corredor_1]
    for i in range(1,6):
        melhor_volta_corredor_i = min(matriz[i])
        if melhor_volta_corredor_i < melhor_performance [1]:
            corredor = i + 1
            melhor_volta = melhor_volta_corredor_i
            volta = matriz[i].index(melhor_volta) + 1
            melhor_performance[0] = corredor
            melhor_performance[1] = melhor_volta
            melhor_performance[2] = volta
    return tuple(melhor_performance)