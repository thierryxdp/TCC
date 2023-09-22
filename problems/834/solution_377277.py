def media_matriz(m):
    """função que recebe uma matriz (m) e que calcula a média de cada
    elemento da matriz. E que deve retornar os números com duas casas
    decimas;
    matriz->matriz"""
    linhas = range(len(m))
    matriz = m[:]
    for i in linhas:
        colunas = range(len(m[0]))
        for j in colunas:
            matriz[i][j] = round(matriz[i][j]/len(m[0]),2)
    return matriz