def eh_quadrada (matriz):
    """Analisa se uma matriz dada de entrada é quadrada ou não"""
    if len (matriz) == len (matriz[0]):
        mensagem = True
    elif len (matriz)==0 and len (matriz[0])==0:
        mensagem = True
    else:
        mensagem = False
    return mensagem