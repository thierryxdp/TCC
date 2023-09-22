def media_matriz(matriz):
    ''''''
    linhas = len(matriz)
    colunas = len(matriz[0])
    soma = 0
    for i in range(linhas):
            soma += sum(matriz[i])
        numero=soma/(colunas*linhas)
        return round(numero,2)