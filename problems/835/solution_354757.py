def melhor_volta(matriz):
    '''
    list -> tuple'''
    melhorVolta = []
    for i in range(len(matriz)):
        melhorVolta.append(min(matriz[i]))
        
    tempo = min(melhorVolta)
    melhorCompetidor = melhorVolta.index(tempo)+1
    voltaN = matriz[melhorCompetidor-1].index(tempo)+1

    return (melhorCompetidor, tempo, voltaN)