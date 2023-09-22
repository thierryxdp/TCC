def melhor_vola(matriz):
    """ """
    i = 0
    l = []
    for i in matriz:
        rapido=min(i)
        l.append(rapido)
    	melhor_volta=min(l)
   		vencedor=l.index(melhor_volta)
    	volta=matriz[vencedor].index(melhor_volta)
    return vencedor+1,melhor_volta,volta+