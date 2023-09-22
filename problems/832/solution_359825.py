def eh_quadrada(matriz):
    """ Dada uma matriz diz se ela é quadrada;
    list -> bool"""
    resposta = ''
    if matriz == []:
        resposta == True
        elif len(matriz) == len(matriz[0]):
            resposta = Tru
        else:
            resposta = False
    return resposta