def eh_quadrada(matriz):
    '''Retorna True para caso a matriz seja quadrado e False caso contrário
list -> bool'''
    linhas=len(matriz)
    colunas=len(matriz[0])
    if linhas==colunas:
        return True
    else:
        return False