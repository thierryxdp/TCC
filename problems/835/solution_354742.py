def melhor_volta(matriz):
    '''
    list -> tuple'''
    melhorVolta = []
    for i in range(matriz):
        melhorVolta.append(min(matriz[i]))
        
    tempo = min(melhorVolta)
    melhorCompetidor = matriz.index(tempo)+1
    voltaN = matriz.index(melhorCompetidor-1)

    return (melhorCompetidor, tempo, voltaN)