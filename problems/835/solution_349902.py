def melhor_volta(matriz):
    melhores = []
    for i in matriz:
        melhores = melhores + min(i)
    return melhores