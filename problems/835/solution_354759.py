def melhor_volta(matriz):
    '''Dada uma matriz com os tempos dos corredores em uma corrida de Kart retorna uma tupla com contendo o melhor competidor, qual o seu tempo e em que volta
    list -> tuple'''
    melhorVolta = []
    for i in range(len(matriz)):
        melhorVolta.append(min(matriz[i]))
        
    tempo = min(melhorVolta)
    melhorCompetidor = melhorVolta.index(tempo)+1
    voltaN = matriz[melhorCompetidor-1].index(tempo)+1

    return (melhorCompetidor, tempo, voltaN)