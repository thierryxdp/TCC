def melhor_volta(matriz):
    menor_tempo_corredor = []  
    for corredor in range(len(matriz)):
        list.append(menor_tempo_corredor, min(matriz[corredor]))
    menor_tempo_total = min(menor_tempo_corredor)
    corredor_mais_rapido = list.index(menor_tempo_corredor, menor_tempo_total)
    volta_mais_rapida = list.index(matriz[corredor_mais_rapido], menor_tempo_total)
    return (corredor_mais_rapido+1, menor_tempo_total ,volta_mais_rapida+1)