def melhor_volta(matriz):
    melhores_vol=[]
    corredor=0
    for linha in matriz:
        mini_lin=min(linha)
        list.append(melhores_vol,mini_lin)
    corredor=list.index(melhores_vol,min(melhores_vol))
    return corredor