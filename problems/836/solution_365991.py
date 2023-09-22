def busca(Setor,Funcionarios):
    t=[]
    for i in range(len(Funcionarios)):
        for c in range(len(Funcionarios[0])):
            if Funcionarios[i][c]==Setor:
                	Funcionarios[c].remove(Setor)
                	t.append(Funcionarios[i][c])
    	return t