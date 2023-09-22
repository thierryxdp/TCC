def media_matriz(matriz):
    """funcao que dada de entrada uma matriz de inteiros não
    vazia, retorna a média de todos os números da matriz com
    exatamente duas casas decimais de precisão;
    list(list) -> float"""
    
    elementos = []
    for i in range(len(matriz)):
        for n in matriz[i]:
            elementos += [n]
    linhas = len(matriz)
    colunas = len(matriz[0])
    return round((sum(elementos))/(linhas*colunas),2)