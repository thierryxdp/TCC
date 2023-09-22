def busca(setor,matriz):
    funcionarios=[]
    for i in range(len(matriz)):
        if setor==matriz[i][2]:
            funcionarios.append(matriz[i])
    for n in range(len(funcionarios)):
    	list.pop(funcionarios[n],2)
	
    return funcionarios