def busca(setor,matriz):
    encontrados=[]
	for i in range(len(matriz)):
        if (matriz[i][2]==setor):
            encontrados.append(matriz[i][0:2]+matriz[i][3:4])
    return encontrados