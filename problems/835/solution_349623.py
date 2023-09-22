def melhor_volta(matriz):
    lista_melhor_tempo = []
    for corredor in matriz:
        lista_melhor_tempo.append(min(corredor))
    melhor_tempo = min(lista_melhor_tempo)
    corredor_melhor_tempo = lista_melhor_tempo.index(melhor_tempo)
    melhor_volta = lista_melhor_tempo[corredor_melhor_tempo].index(melhor_tempo)
    return corredor_melhor_tempo+1,melhor_tempo,melhor_volta+1