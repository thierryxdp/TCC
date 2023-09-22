def busca(m,setor):
    r = []
    for i in range(len(m)):
        for j in range(len(i)):
            if m[i][j] == setor:
                p = [m[i][0],m[i][1],m[i][3]]
                list.append(r,p)
	return r