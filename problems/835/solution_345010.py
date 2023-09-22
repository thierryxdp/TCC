def melhor_volta(matriz):
    '''dada uma matriz com tempos dos corredores de uma corrida, retorna uma tupla com o corredor que obteve a melhor volta, on tempo e em qual volta isso ocrreu
    list -> tuple'''
    tempo_volta = []
    Tempo = []
    for corredor in matriz:
        list.append(tempo_volta, [min(corredor) , list.index(corredor, min(corredor))+1])
    for dupla in tempo_volta:
        list.append(Tempo, dupla[0])
    mel_tempo = min(Tempo)
    mel_corredor = list.index(Tempo, mel_tempo) + 1
    mel_volta = tempo_volta[mel_corredor - 1][1]
    return mel_corredor, mel_tempo,   mel_volta