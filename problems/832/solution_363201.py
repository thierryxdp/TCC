def eh_quadrada(matriz):
    '''funçao que dada uma matriz retornar se ela é quadrada.
list ->bool'''
    linha=len(matriz)
    coluna=len(matriz[0])
    if linha==0:
        return True
    if coluna==linha:
        return True
    else:
        return False