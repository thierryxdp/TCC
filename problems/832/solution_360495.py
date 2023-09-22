def eh_quadrada(matriz):
    '''Retorna True para caso a matriz seja quadrado e False caso contrário
list -> bool'''
    linhas=len(matriz)
    if linhas==0:
        colunas=0
    else:
        colunas=len(matriz[0])
    if linhas==colunas:
        return True
    else:
        return Fal