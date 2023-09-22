def eh_quadrada(matriz):
    '''Função que diz se uma matriz e quadrada.list->bool'''
    if any(len(linha) != len(matriz) for linha in matriz):
          return False
    for i in range(len(matriz)):
         for j in range(i):
                if matriz[i][j] != matriz[j][i]:
                    return False
    if len(matriz)==4:
        return True
    return True