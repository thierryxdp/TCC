def media_matriz(matriz):
    """Função que dada uma matriz de inteiros não vazia, retorna a média 
       de todos os números da matriz(com exatamente duas casas decimais de
       precisão).
       list -> int
       
       Parâmetros:
       matriz: A matriz que será verificada a média de todos os seus 
               números.
       
       Returns: A média de todos os números da matriz(com exatamente duas 
                casas decimais de precisão)
    """
    soma = 0
    numerotermos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma += matriz[i][j]
            numerotermos += 1
    return round(soma/numerotermos,2)