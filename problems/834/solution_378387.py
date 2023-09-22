def media_matriz(matriz):
    """ A função media_matriz, dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz (com exatamente duas casas decimais de precisão).
   list --> int"""
    nlin = len(matriz)
    if nlin == 0:
        return 0
    ncol = len(matriz[0])
    acumulador = 0
    for i in range(nlin):
        for j in range(ncol):
            acumulador += matriz[i][j]
    return round(acumulador/(nlin*ncol),2)