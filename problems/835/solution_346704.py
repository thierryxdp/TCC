def melhor_volta(matriz):
    listaMin = []
    infos = ()
    for i in range(6):
        minimo = min(matriz[i])
        listaMin.append(minimo)
    menorTempo = min(listaMin)
    jogador = listaMin.index(menorTempo)+1
    posNaMatriz = listaMin.index(menorTempo)
    indice = matriz[posNaMatriz].index(menorTempo)+1
    infos = (jogador,menorTempo,indice)
    return infos