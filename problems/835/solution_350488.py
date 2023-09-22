def melhor_volta(matriz):
    """Funcao que recebe uma matriz 6 x 10 com os tempos
    em segundos dos seis corredores em suas dez voltas, e
    retorna uma tupla informando de quem foi a melhor volta,
    com qual tempo e em que volta;
    list[list] -> tuple"""
    melhor_tempo_cada_corredor=[]
    for corredor in matriz:
        melhor_tempo_cada_corredor+=[min(corredor)]
    melhor_tempo_total=min(melhor_tempo_cada_corredor)
    melhor_corredor=list.index(melhor_tempo_cada_corredor,melhor_tempo_total)
    melhor_volta_total=list.index(matriz[melhor_corredor],melhor_tempo_total)
    return (melhor_corredor+1,melhor_tempo_total,melhor_volta_total+1)