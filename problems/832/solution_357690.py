def eh_quadrada(matriz):
    '''Funcao que ao receber uma matriz, retorna True se ela for
quadrada e retorna False caso nao seja. list-> bool'''
    linha= len(matriz)
    coluna= len(matriz[0])
    if linha == coluna:
        return True
    else:
        return False