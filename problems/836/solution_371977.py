def busca(setor,matriz):
    l=[]
	for x in matriz:
        if x[2]==setor:
            l.append(x[0],x[1],x[3])
	return l