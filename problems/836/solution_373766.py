def busca(setor,matriz):
	d=[]
    for i in matriz:
        for j in i:
            if j==setor:
                d.append(i)
   	return d[0:]