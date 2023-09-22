def melhor_volta(matriz):
    tempo=[]
    volta=1 
    for L in range(0,6):
        for C in range(0,10):
            list.append(tempo,matriz[L][C])
            if matriz[L][C]==min(tempo):
                jog=list.index(matriz,matriz[L])+1
    volta=volta+1
    return jog,matriz[L][C],volta