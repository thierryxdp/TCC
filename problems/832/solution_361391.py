def eh_quadrada (matriz):
    """Analisa se uma matriz dada de entrada é quadrada ou não"""
    if matriz == []:
        mensagem = True
    elif len (matriz) == len (matriz[0]):
        mensagem = True
    else:
        mensagem = False
    return mensagem