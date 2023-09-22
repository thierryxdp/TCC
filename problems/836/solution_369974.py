def busca(nome,matriz):
    """Dado uma matriz com informações de funcionários e uma paçavra de busca, retorna a lista que possua essa palavra. list,string>list"""
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