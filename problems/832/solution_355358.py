def eh_quadrada(matriz):
    '''função que verifica se uma matriz é quadrada, ou seja, se possui o mesmo número de linhas e colunas, a partir de uma matriz de entrada; list(lists) -> bool'''
    
    for i in range(len(matriz)):
                   for j in range(len(matriz[0])):
                                  if i == 0 and j == 1:
                                  return True