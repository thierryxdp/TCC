def melhor_volta(matriz):
    '''função que dada uma matriz 6 x 10 com os tempos dos corredores em
    segundos de cada volta, retorna de quem foi a melhor volta, com qual
    tempo e em que volta; list(list) -> tuple'''
    melhor = min(matriz[0])
    volta = 1
    quem = list.index(matriz[volta-1],melhor)
    for linha in matriz:
        if melhor > min(linha):
            melhor = min(linha)
            volta = list.index(matriz,linha)+1
            quem = list.index(matriz[volta-1],melhor)+1
    return (quem, tempo, volta)