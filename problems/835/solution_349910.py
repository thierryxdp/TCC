def melhor_volta(matriz):
    melhores = []
    for i in range(len(matriz)):
        melhores = melhores + [min(matriz[i])]
        melhor = min(melhores)
    volta = 0
    i = 0
    lista = matriz[i]
    while i < len(matriz):
        if melhor in matriz[i]:
            volta = volta + lista.index(melhor)
    return (melhores.index(melhor))+1,melhor