def melhor_volta(matriz):
    tempo=[]
    volta=0 
    for L in range(1,7):
        for C in range(1,11):
            list.append(tempo,matriz[L][C])
            if matriz[L][C]==min(tempo):
                jog=list.index(matriz,matriz[L])
             
    volta=volta+1
    return jog,matriz[L][C],volta