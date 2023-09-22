def busca(setor,matriz):
    lista=[]
    for i in matriz:
        if setor in i:
            lista.append(i)
    	for j in lista:
            lista.remove(setor)
    return lista