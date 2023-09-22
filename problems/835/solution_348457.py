def melhor_volta(matriz):
    '''diz qual piloto obteve o menor tempo em 1 lap, o
    tempo do lap e  qual o lap; list -> tuple'''
    piloto = len(matriz)
    laps = len(matriz[0])
    b = []
    t = 0
    c = 0
    b1 = min(matriz[0])
    b2 = min(matriz[1])
    b3 = min(matriz[2])
    b4 = min(matriz[3])
    b5 = min(matriz[4])
    b6 = min(matriz[5])
    for p in range(piloto):
        b.append(b1)
        b.append(b2)
        b.append(b3)
        b.append(b4)
        b.append(b5)
        b.append(b6)
        for l in range(laps):
        	t += min(b)
            c += b.index(min(b))
            return (p+1,t,c+1)