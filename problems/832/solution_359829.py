def eh_quadrada(matriz):
    """ Dada uma matriz diz se ela é quadrada;
    list -> bool"""
    resposta = ''
    if matriz == []:
        return True
    if len(matriz) == len(matriz[0]):
        resposta = True
    else:
        resposta = False
    return resposta