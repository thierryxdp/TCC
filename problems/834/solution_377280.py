def media_matriz(m):
    """função que recebe uma matriz (m) e que calcula a média de cada
    elemento da matriz. E que deve retornar os números com duas casas
    decimas;
    matriz->matriz"""
    linhas = len(m)
    soma = 0
    for i in range(linhas):
        colunas = len(m[0])
        for j in range(colunas):
            soma = soma +m[i][j]
    soma = round(soma/(linhas*colunas),2)
    return soma