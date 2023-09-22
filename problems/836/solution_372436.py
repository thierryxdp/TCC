def busca(setor,matriz):
    resultado = []
    i = -1
    for linha in matriz:
        i += 1
        for coluna in linha:
            
            if coluna == setor:
                lista = []
                lista.append(matriz[i][0])
                lista.append(matriz[i][1])
                lista.append(matriz[i][3])
                
                resultado.append(lista)
                
	return resultado