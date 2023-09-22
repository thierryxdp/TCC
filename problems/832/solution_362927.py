def eh_quadrada(matriz):
    '''Funcao que recebe uma matriz e identifica se ela é 
       quadrada, ou não. Ou seja, quando a matriz tem a 
       mesma quantidade de linhas e colunas.
       : param matriz: list
       : return: bool
    '''
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
            if (nlin==ncol):
                  return 'True'
            if (nlin==[]):
                  return 'True'
    return 'False'