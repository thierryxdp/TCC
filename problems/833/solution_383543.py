def transposta(matriz):
    nLinhas= len(matriz)
    nColunas = len(matriz[0])
    mNova = []
    for i in range (nColunas):
        mNova.append([0]*nLinhas)
    for i in range(0,nLinhas):
        for j in range(0,nColunas):
            mNova[j][i] = matriz[i][j]
    return mNova