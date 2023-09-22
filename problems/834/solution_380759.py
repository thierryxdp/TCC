def media_matriz(matriz):
    """Recebe uma matriz e retorna a média de todos os números dela, 
    com duas casas decimais de precisão.
    assinatura: list --> int
    testes:
    """
    res = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            res = res + (i + j)/2
	return res