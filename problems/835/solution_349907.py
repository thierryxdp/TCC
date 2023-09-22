def melhor_volta(matriz):
    melhores = []
    for i in range(len(matriz)):
        melhores = melhores + [min(matriz[i])]
        melhor = min(melhores)
    return (melhores.index(melhor))+1,melhor