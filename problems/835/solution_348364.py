def melhor_volta(m):
    for elementos in m:
        menorTempo=min(elementos)
        volta=list.index(elementos, menorTempo)
    return menorTempo,volta