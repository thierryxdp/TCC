def busca(setor:str,m:list)->list:
	matriz=[]
    for i in range(len(m)):
        if setor in m[i][2]:
            m1=[]
            m1.append(m[i][0])
            m1.append(m[i][1])
            m1.append(m[i][3])
            matriz.append(m1)
   	return matriz