def melhor_volta(matriz):
    '''dada uma matriz representando os tempos de laps de 
    corredores, retorna uma tupla com valores: atleta com 
    melhor tempo e o tempo do lap; list -> tuple'''
    atletas = len(matriz)
    laps = len(matriz[0])
    for a in range(atletas):
        for l in range(laps):
            t = min(matriz[i][j])
            return (i,t)