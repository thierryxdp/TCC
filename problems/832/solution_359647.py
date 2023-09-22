def eh_quadrada(matriz):
    '''Função que diz se uma matriz e quadrada.list->bool'''
    if any(len(linha) != len(mat) for linha in mat):
          return False
    for i in range(len(mat)):
         for j in range(i):
                if mat[i][j] != mat[j][i]:
                    return False
    return True