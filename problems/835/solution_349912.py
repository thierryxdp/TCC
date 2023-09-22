def melhor_volta(matriz):
    melhores = []
    for i in range(len(matriz)):
        melhores = melhores + [min(matriz[i])]
        melhor = min(melhores)
    volta = 0
    i = 0
    while i < len(matriz):
        if melhor in matriz[i]:
            lista = matriz[i]
            volta = volta + lista.index(melhor)
            i = i + 1
    return (melhores.index(melhor))+1,melhor