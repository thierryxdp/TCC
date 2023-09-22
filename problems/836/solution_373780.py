def busca(setor, matriz):
    """
    Ao inserir um setor e uma matriz, retornará a informação desse setor.
    str,list-> list
    """
    resultado = []
    for i in range(len(matriz)):
    	if matriz[i][2]== setor:
            list.pop(matriz[i],2)
            resultado.append(matriz[i])
	return resultado