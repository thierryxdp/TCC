def melhor_volta(matriz):
    """ A função melhor_volta, dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz (com exatamente duas casas decimais de precisão).
        
        Parameters:
        matriz = matriz de numeros inteiros a ser analisada

        Testes:
            melhor_volta ([[1,1],[2,3]]) == 2
            melhor_volta ([]) == 0
            melhor_volta ([[1,1,2,3,4,5,6]]) == 2
            melhor_volta ([[1],[2],[1],[3],[5],[1]]) == 3

        Returns:
            média de todos os números da matriz (com exatamente duas casas decimais de precisão).
            int, list --> int
    """
    nlin = len(matriz)
    ncol = len(matriz[0])
    menor_tempo = min(matriz)
    for i in range(nlin):
        for j in range(ncol):
            if matriz [i][j] == menor_tempo:
                return (i+1,menor_tempo,j+1)