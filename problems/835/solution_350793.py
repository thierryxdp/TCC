def melhor_volta(tempos):
    '''Retorna uma tupla que contém o número do corredor com a melhor volta, o tempo da melhor volta e qual volta foi.
    list(list)->tuple'''
    quant_corredores=len(tempos)
    quant_voltas=len(tempos[0])
    melhor_tempo_corredor=0
    melhor_tempo_volta=0
    tempo_s=[]
    for corredor in range(quant_corredores):
        for volta in range(quant_voltas):
            list.append(tempo_s,tempos[corredor][volta])
            if min(tempo_s)==tempos[corredor][volta]:
                melhor_tempo_corredor=corredor +1
                melhor_tempo_volta=volta +1
    return (melhor_tempo_corredor, melhor_tempo_volta, min(tempo_s))