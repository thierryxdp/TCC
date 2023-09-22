def melhor_volta(matriz):
    '''função que dada uma matriz 6 x 10 com os tempos dos corredores em
    segundos de cada volta, retorna de quem foi a melhor volta, com qual
    tempo e em que volta; list(list) -> tuple'''
    melhor = min(matriz[0])
    quem = 1
    volta = list.index(matriz[quem-1],melhor)+1
    for linha in matriz:
        if melhor > min(linha):
            melhor = min(linha)
            quem = list.index(matriz,linha)+1
            volta = list.index(matriz[quem-1],melhor)+1
    return (quem, melhor, volta)