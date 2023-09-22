def melhorvolta(matriz):
    'dadas as informações de cada volta de cada corredor, returna uma tupla informando qual foi o corredor mais rapido e em qual volta. list -> tuple'
    melhortempo = min(min(matriz))
    i=0
    while melhortempo not in matriz[i]:
        i=i+1
    return (i+1,melhortempo)