def eh_quadrada(matriz):
    '''Função booleana que identifica se uma matriz é quadrada ou não; list-> bool'''
    if matriz==[[]]:
        return True
    elif linhas == colunas:
        linhas= len(matriz)
        colunas=len(matriz[0])
        return True
    else:
        return False