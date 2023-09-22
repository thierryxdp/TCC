def media_matriz(matriz):
    '''Função que dada uma matriz retornará a média da soma de todos os termos da matriz
    matrix -> float'''

    soma_elementos = 0

    if len(matriz) != 0:
      '''Se a matriz não for vazia'''
      for linha in matriz:
        '''Para cada elemento da matriz (linha)'''
        for elemento in linha:
          '''Para cada elemento de cada linha (coluna), o elemento é somado,
          e a soma de todos os elementos é dividida pela quantidade de elementos (média)'''
          soma_elementos += elemento
        media_elementos = soma_elementos / (len(matriz[0])*len(matriz))

    return round(media_elementos,2)