def busca(setor,m):
    matriz = []
    for i in range(len(m)):
   		if setor in m[i][2]:
         	matriz.append(m[i][:2]+m+[1[3:]])
    return matriz