def busca (setor, matriz):
    """Função que, dado um setor e uma matriz de dados, retorna todos os funcionários daquele setor.
    Entrada: string e lista.
    Saída: lista."""
    
    encontrado = []
    
	for i in range(len(matriz)):
		if matriz[i][2] == setor:
            del matriz[i][2]
    		list.append(encontrado, matriz[i])
    return encontrado