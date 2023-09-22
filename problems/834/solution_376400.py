def media_matriz(matriz):
    """ A função media_matriz, dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz (com exatamente duas casas decimais de precisão).
        
        Parameters:
        matriz = matriz de numeros inteiros a ser analisada

        Testes:
            media_matriz ([[1,1],[2,3]]) == 2
            media_matriz ([]) == 0
            media_matriz ([[1,1,2,3,4,5,6]]) == 2
            media_matriz ([[1],[2],[1],[3],[5],[1]]) == 3

        Returns:
            média de todos os números da matriz (com exatamente duas casas decimais de precisão).
            int, list --> int
    """
    nlin = len(matriz)
    if nlin == 0:
        return 0
    ncol = len(matriz[0])
    acumulador = 0
    for i in range(nlin):
        for j in range(ncol):
            acumulador += matriz[i][j]
    return round(acumulador/(nlin*ncol),2)