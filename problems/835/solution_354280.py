def melhor_volta(matriz):
    melhores = []
    for i in range(len(matriz)):
        melhores.append( min(matriz[i]) )
    melhor_corredor = melhores.index( min(melhores) )
    melhor_volta = matriz[melhor_corredor].index( min(matriz[melhor_corredor]) )
    return melhor_corredor+1, melhor_volta+1