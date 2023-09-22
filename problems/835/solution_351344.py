def melhor_volta(matriz):
    '''Função que, dada uma matriz 6x10 que informa os tempos de voltas de cada corredor como entrada, retorna de quem foi a melhor volta da prova e o tempo da volta; list[list] -> tuple'''
    melhor_tempo=[]
    for corredor in matriz:
        list.append(melhor_tempo,min(corredor))
        melhor_tempo_total=min(melhor_tempo)
    melhor_corredor=list.index(matriz,melhor_tempo_total)
    melhor_volta=list.index(