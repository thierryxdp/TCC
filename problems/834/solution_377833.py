def media_matriz(matriz:list)->list:
    '''retorna a média de todos os números da matriz dada de parâmetro'''
    soma = 0
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            soma = soma + matriz[i][j]
    resultado = soma/(linhas*colunas)
    return round(resultado,2)