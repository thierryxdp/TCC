def busca(setor:str,m:list)->list:
    lista=[]
    for i in range(len(m)):
    	for j in range(len(m[i][2])):
            if setor==(m[i][2]):
                lista.append(m[i])
	return lista