def melhor_volta(matriz):
    lista=[]
    for corredor in matriz:
        menorTempo=min(corredor)
        lista.append(corredor)
        lista.append(menorTempo)
    return lista