def busca(setor:str,m:list)->list:
	matriz=[]
    for i in range(len(m)):
        if setor in m[i][2]:
            matriz.append(m[i])
            matriz.remove(m[i][2])
    return matriz