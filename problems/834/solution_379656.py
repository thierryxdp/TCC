def media_matriz(M):
    """Recebe uma matriz de inteiros não vazia e retorna a
média de todos os elementos contidos dentro da matriz com
precisão de até duas casas decimais.
mat -> float
"""
    lista_numeros = []
    for linhas in M:
        for colunas in linhas:
            list.append(lista_numeros, colunas)
    return round(sum(lista_numeros)/len(lista_numeros), 2)