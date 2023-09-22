def media_matriz(matriz_inteiros2):
    """Função que dada uma matriz de numeros inteiros nao vazia, me retorna
a media de todos os numeros que estao nessa matriz, somente com duas casas decimais
 list--> float."""
    colunas = len(matriz_inteiros2[0])
    linhas = len (matriz_inteiros2)
    elementos = 0
    for i in range(len(matriz_inteiros2)):
        elementos = sum(matriz_inteiros2[i])
        quant_elementos = colunas*linhas
    mediaMatriz = elementos/quant_elementos
    return round (mediaMatriz,2)