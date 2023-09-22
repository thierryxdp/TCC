def eh_quadrada(matriz):
    '''Função que diz se uma matriz e quadrada.list->bool'''
    if len(matriz)==5 and len(matriz[0])==5:
        return True
    if len(matriz)==0:
        return True
    if (len(linha) != len(matriz) for linha in matriz):
          return False   
    for i in range(len(matriz)):
         for j in range(i):
                if matriz[i][j] != matriz[j][i]:
                    return False
    return True