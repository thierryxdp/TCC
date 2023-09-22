def media_matriz(matriz):
    ''' Função que recebe uma matriz não vazia e retorna a média de todos os números da matriz; list(list)->int'''
    soma=0
    colunas=len(matriz[0])
    linhas= len(matriz)
    for linha in matriz:
        for aij in linha:
            soma=soma+aij
            media= round(soma/(linhas*colunas),2)
    return media