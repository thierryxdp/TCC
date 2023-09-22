def busca(setor:str,m:list)->list:
    lista=[]
    for i in range(len(m)):
    	for j range(len(m[i][0])):
            if setor==(m[i][0]):
                lista.append(m[i])
	return lista