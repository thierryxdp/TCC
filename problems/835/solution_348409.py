def melhor_volta(matriz):
    '''diz qual piloto obteve o menor tempo em 1 lap e o
    tempo do lap; list -> tuple'''
    piloto = len(matriz)
    laps = len(matriz[0])
    a = []
    a1 = min(matriz[0])
    a2 = min(matriz[1])
    a3 = min(matriz[2])
    a4 = min(matriz[3])
    a5 = min(matriz[4])
    a6 = min(matriz[5])
    for p in range(piloto):
        a.append(a1)
        a.append(a2)
        a.append(a3)
        a.append(a4)
        a.append(a5)
        a.append(a6)
        for l in range(laps):
            t == min(a)
            return (p+1,t)