def busca(nome,matriz):
    x=[]
    y=0
    for a in matriz:
        for b in a:
            if b==nome:
         		list.append(x,matriz[y])
                matriz[y].remove(nome)
    	y+=1
    
    return x