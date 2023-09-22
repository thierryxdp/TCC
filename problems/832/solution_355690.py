def eh_quadrada(matriz):
    '''Função booleana que identifica se uma matriz é quadrada ou não; list-> bool'''
    linhas= len(matriz)
    colunas=len(matriz[0])
    if linhas == colunas or matriz==[[]]:
        return True
    else:
        return False