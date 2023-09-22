def melhor_volta(matriz):
	i=0
    for corredores in matriz:
        menorTempo=min(corredores)
        i=list.index(corredores,menorTempo)
    return menorTempo,i