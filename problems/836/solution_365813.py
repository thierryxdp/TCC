def busca (setor, matriz):
    """Função que, dado um setor e uma matriz de dados, retorna todos os funcionários daquele setor.
    Entrada: string e lista.
    Saída: lista."""
    
    encontrado = []
    

	if matriz[0][2] == setor:
        del matriz[0][2]
    	list.append(encontrado, matriz[0])
    if matriz[1][2] == setor:
        del matriz[1][2]
        list.append(encontrado, matriz[1])
    if matriz[2][2] == setor:
        del matriz[2][2]
        list.append(encontrado, matriz[2])
    return encontrado