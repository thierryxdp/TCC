def busca(setor,matriz):
    funcionarios=[]
    for i in range(len(matriz)):
        if setor==matriz[i][2]:
            funcionarios.append(matriz[i])
            funcionarios[i].pop(2)
	
    return funcionarios