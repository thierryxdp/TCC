def melhor_volta(m):
    Todos=[]
	cadaCorredor=[]
    i=0
    lista=[]
    for elementos in m:
        menorTempo=min(elementos)
        volta=list.index(elementos, menorTempo)
        cadaCorredor.append(menorTempo)
        cadaCorredor.append(volta)
        lista.append(list(cadaCorredor))
    return lista