def melhor_volta(matriz):
    melhores = []
    for i in range(len(matriz)):
        melhores = melhores + min(i)
    return melhores