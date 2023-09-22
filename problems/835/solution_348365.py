def melhor_volta(m):
    for elementos in m:
        menorTempo=min(elementos)
        volta=list.index(elementos, menorTempo)
        cadaCorredor.append(menorTempo)
        cadaCorredor.append(volta)
    return cadaCorredor