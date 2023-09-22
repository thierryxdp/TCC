def melhor_volta(matriz):
    '''diz qual piloto obteve o menor tempo em 1 lap, o
    tempo do lap e  qual o lap; list -> tuple'''
    piloto = len(matriz)
    laps = len(matriz[0])
    b = []
    t = 0
    c = 0
    d = 0
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
       		c.append(matriz[b.index(t)])
            d += min(c)
            return (b.index(t)+1,t,+1)