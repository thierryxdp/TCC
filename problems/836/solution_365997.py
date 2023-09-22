def busca(Setor,Funcionarios):
    t=[]
    for i in range(3):
        for c in range(4):
            if Funcionarios[i][c]==Setor:
                	t.append(Funcionarios[c])
    	return t