def media_matriz(matriz):
    linhas = (len(matriz))
    colunas = (len(matriz[0]))
    soma = 0
    media = ()
    for elementos in matriz:
        for number in elementos:
            soma = soma + number
    media = (soma/(colunas*linhas))
    return media