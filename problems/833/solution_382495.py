def conta_numero(numero, matriz):
    """ Retorna quantas vezes o numero dado aparece na matriz dada;
        Entrada: int, list;
        Saida: int;
     """
    resultado = 0
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j]==numero:
                resultado += 1
    return resultado
	if matriz == []:
        return acumulador