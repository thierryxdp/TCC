def busca(setor,M):
    lista=[]
    for i in range(len(M)):
        for j in range(len(M[0])):
        	if setor in M[i][j]:        
                list.append(lista,M[i]) 
    for i in range(len(lista)):
    	while setor in lista[i]:
        	list.remove(lista[i],setor)               
    return lista