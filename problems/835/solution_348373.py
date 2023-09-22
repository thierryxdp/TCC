def melhor_volta(m):
    Todos=[]
	cadaCorredor=[]
    i=0
    for elementos in m:
        menorTempo=min(elementos)
        volta=list.index(elementos, menorTempo)
        cadaCorredor.append(menorTempo)
        cadaCorredor.append(volta)
        cadaCorredor.append(i)
        i+=1
        lista+=cadaCorredor
    return