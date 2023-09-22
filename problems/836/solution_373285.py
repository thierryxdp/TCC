def busca(setor,matriz):
    funcionarios=[]
    for i in range(len(matriz)):
        if setor==matriz[i][2]:
            funcionarios.append(matriz[i][0:2]+matriz[3])
	
    return funcionarios