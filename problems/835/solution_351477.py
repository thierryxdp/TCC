def melhor_volta(matriz):
    '''Função que, dada uma matriz 6x10 que informa os tempos de voltas de cada corredor como entrada, retorna de quem foi a melhor volta da prova e o tempo da volta; list[list] -> tuple'''
    melhores_tempos=[]
    melhores_voltas=[]
    for corredor in matriz:
        melhor_tempo=min(corredor)
        list.append(melhores_tempos,melhor_tempo)
        melhor_volta=list.index(corredor,melhor_tempo)
        list.append(melhores_voltas,melhor_volta)
    melhor_tempo_geral=min(melhores_tempos)
    melhor_corredor=list.index(melhores_tempos,melhor_tempo_geral)
    melhor_volta_geral=melhores_voltas[melhor_corredor]
    resultado=(melhor_corredor+1,melhor_tempo_geral,melhor_volta_geral+1)
    return resultado