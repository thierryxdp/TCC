def busca(setor, matriz):
    """Função que busca por informações de um determinado setor em uma matriz;
    str,list->list"""
    resultado = []
    for i in range(len(matriz)):
    	if matriz[i][2]== setor:
            list.pop(matriz[i],2)
            resultado.append(matriz[i])
	return resultado