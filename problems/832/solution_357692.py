def eh_quadrada(matriz):
    '''Funcao que ao receber uma matriz, retorna True se ela for
quadrada e retorna False caso nao seja. list-> bool'''
    linha= len(matriz)
    if linha == 0:
        return True
    coluna= len(matriz[0])
    elif linha == coluna:
        return True
    else:
        return False