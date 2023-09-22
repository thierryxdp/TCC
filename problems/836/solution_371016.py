def busca(setor:str,m:list)->list:
	matriz=[]
    for i in range(len(m)):
        if setor in m[i][2]:
            m1=[]
            matriz.append(m[i][0])
            matriz.append(m[i][1])
            matriz.append(m[i][3])
            m1.append(matriz)
    return m1