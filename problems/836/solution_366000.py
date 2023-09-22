def busca(Setor,Funcionarios):
    t=[]
    for i in range(len(Funcionarios)):
        for c in range(len(Funcionarios[0])):
            if Funcionarios[i][c]==Setor:
                t.append(Funcionarios[i][c])
   		return t