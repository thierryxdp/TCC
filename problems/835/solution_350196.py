def melhor_volta(matriz):
	melhorlista=min(matriz)
    melhortempo=min(melhorlista)
    melhorvolta=melhorlista.index(melhortempo)+1
    melhorcorredor=matriz.index(melhorlista)+1
    t=(melhorcorredor,melhortempo,melhorvolta)
    return t