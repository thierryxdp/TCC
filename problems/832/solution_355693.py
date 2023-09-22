def eh_quadrada(matriz):
    '''Função booleana que identifica se uma matriz é quadrada ou não; list-> bool'''
    if matriz==[[]]:
        return True
    linhas= len(matriz)
    colunas=len(matriz[0])
    elif linhas == colunas:
        return True
    else:
        return False