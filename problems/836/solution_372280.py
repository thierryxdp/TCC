def busca(setor:str,m:list)->list:
    lista=[]
    for i in range(len(m)):
    	for j in range(len(m[i][0])):
            if setor==(m[i][j]):
                lista.append(m[i])
	return lista