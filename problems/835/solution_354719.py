def melhor_volta(matriz):
    vencedor = matriz[0]
    melhor = matriz[0,0]
    for corredor in matriz:
        if min(corredor) < melhor:
            vencedor = list.index(matriz,corredor)
            melhor = min(corredor)
    return (vencedor+1,melhor,list.index(matriz[vencedor],melhor)+1)