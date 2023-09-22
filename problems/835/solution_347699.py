def melhor_volta(matriz):
    """ função que recebe como entrada uma matriz 6x10, 
    onde cada linha representa um corredor e as colunas o
    tempo em segundos dos corredores em cada volta. A
    função retorna de quem foi a melhor volta, o seu
    tempo e em que volta.
    list -> tuple"""

    melhor_tempo = []
    volta = []

    for linha in matriz:
        melhor_tempo += [min(linha)]
        for linha in matriz:
            melhor_volta = min(melhor_tempo)
            melhor_corredor = 1 + melhor_tempo.index(melhor_volta)

    tentativa = matriz[melhor_corredor-1].index(melhor_volta)
        
    return melhor_corredor, melhor_volta, tentativa + 1