def melhor_volta(matriz):
    '''dada uma matriz com tempos dos corredores de uma corrida, retorna uma tupla com o corredor que obteve a melhor volta, on tempo e em qual volta isso ocrreu
    list -> tuple'''
    Tempos = []
    Voltas = []
    for corredor in matriz:
        list.append(Tempos, min(corredor))
        list.append(Voltas, list.index(Tempos, min(corredor))+1)
    melhor_tempo = min(Tempos)
    melhor_voltA = list.index(Voltas, melhor_tempo)
    melhor_corredor = list.index(Tempos, melhor_tempo) + 1
    return (melhor_corredor, melhor_tempo, melhor_voltA)