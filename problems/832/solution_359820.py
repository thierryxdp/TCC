def eh_quadrada(matriz):
    """ Dada uma matriz diz se ela é quadrada;
    list -> bool"""
    resposta = ''
    if matriz == []:
        resposta = True
    linhas = len(matriz)
    colunas = len(matriz[0])
    resposta = ''
    if linhas == colunas:
        resposta = True
    else:
        resposta = False
    return resposta