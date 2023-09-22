def melhor_volta(matriz):
    '''Retorna, a partir da matriz, uma tupla informando de quem
    foi a melhor volta da prova, com qual tempo e em que volta'''
    '''List -> tuple'''
    melhor_volta = 0
    tempo = 0
    corredor = 0
    indice = 1
    for i in matriz:
        if min(i) < tempo:
            tempo = min(i)
            corredor = indice
            melhor_volta = i.index(tempo) + 1
        indice += 1
    return (corredor, tempo, melhor_volta)