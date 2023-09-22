def busca(nome,matriz):
    x=[]
    y=0
    for a in matriz:
        for b in a:
            if b==nome:
         		list.append(x,matriz[y])
    	y+=1
	if len(x)==1:
        list.remove(x[0],nome)
    if len(x)==2:
        list.remove(x[0],nome)
        list.remove(x[1],nome)
    return x