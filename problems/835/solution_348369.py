def melhor_volta(m):
    Todos=[]
	cadaCorredor=[]
    i=0
    while i <= len(m):
        menorTempo=min(i)
        volta=list.index(i, menorTempo)
        cadaCorredor.append(menorTempo)
        cadaCorredor.append(volta)
        Todos.append(cadaCorredor)
        i+=1        
    return Todos