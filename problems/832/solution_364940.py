def eh_quadrada(matriz):

    '''Função que identifica se uma matriz é quadrada.
bool -> bool'''
      for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if len(matriz) == len(matriz[lin]) and len(matriz[col]):
                return True
            else:
                return False
        return True