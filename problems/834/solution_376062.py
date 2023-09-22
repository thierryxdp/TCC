def media_matriz (matriz):
    '''Calcula e retorna a média de todos os números presentes na matriz inserida e com precisão de duas casas decmais;
    list -> float'''
    linhas = len(matriz)
    colunas = len(matriz[0])
    total_numeros = linhas*colunas 
    total = 0
    for i in range(linhas):
        for j in range(colunas):
            total += matriz[i][j]
    media = total/total_numeros
    return f"{media:.2f}"