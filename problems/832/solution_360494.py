def eh_quadrada(matriz):
    '''Retorna True para caso a matriz seja quadrado e False caso contrário
list -> bool'''
    linhas=0+len(matriz)
    colunas=0+len(matriz[0])
    if linhas==colunas:
        return True
    else:
        return False