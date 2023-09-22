def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada ou não. Vale ressaltar que
matrizes vazias serão consideradas quadradas
    list -> bool
    '''
    if matriz == list():
        return True
    linhas = len(matriz)
    resposta = True
    for i in range(linhas):
        colunas = len(matriz[i])
        if linhas!=colunas:
            resposta = False
    return resposta