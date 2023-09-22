def eh_quadrada(matriz):
    '''Identifica se uma matriz é quadrada, ou seja, possui mesmo número
    de colunas e linhas
    lista -> bool'''
    linha = 0
    coluna = 0
    for i in range(len(matriz)):
        linha += 1
        for j in range(len(matriz[0])):
            coluna += 1
    if coluna / linha == linha or  coluna / linha == 0 :
        return True
    else:
        return False