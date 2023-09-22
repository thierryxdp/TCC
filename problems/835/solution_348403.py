def melhor_volta(matriz):
    '''diz qual piloto obteve o menor tempo em 1 lap e o
    tempo do lap; list -> tuple'''
    piloto = len(matriz)
    laps = len(matriz[0])
    for p in range(piloto):
        for l in range(laps):
            a = min(matriz[p][l])
            return (p+1, a)