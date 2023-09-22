def eh_quadrada(matriz):
    '''
    Dado uma matriz retorna se a mesma é quadrada ou não.

    Uso:
   eh_quadrada(matriz)

    Entrada:
    - matriz (list): Matriz de informação

     Saída:
    - Retorna True caso a matriz seja quadrada ou False caso não. (bool)
    '''
    if len(matriz) == 0:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False