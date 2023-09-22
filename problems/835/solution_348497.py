def melhor_volta(matriz):
    '''dada uma matriz com os tempos de 10 laps de 6 pilotos,
    retorna uma tupla com o piloto, o tempo e qual foi seu 
    melhor lap; list -> tuple'''
    pilotos = len(matriz)
    laps = len(matriz[0])
    a = []
    t = 0
    c = 0
    w = 0
    b1 = matriz[0]
    b2 = matriz[1]
    b3 = matriz[2]
    b4 = matriz[3]
    b5 = matriz[4]
    b6 = matriz[5]
    for p in range(pilotos):
        a1 = min(b1)
        a2 = min(b2)
        a3 = min(b3)
        a4 = min(b4)
        a5 = min(b5)
        a6 = min(b6)
        a.append(a1)
        a.append(a2)
        a.append(a3)
        a.append(a4)
        a.append(a5)
        a.append(a6)
        for l in range(laps):
            t += min(a)
            w += a.index(min(a))
            if t in b1:
                c += b1.index(a1)
            elif t in b2:    
    			c += b2.index(a2)
            elif t in b3:
                c += b3.index(a3)
            elif t in b4:
                c += b4.index(a4)
            elif t in b5:
                c += b5.index(a5)
            elif t in b6:
                c += b6.index(a6)
	return (w+1, t, c+1)