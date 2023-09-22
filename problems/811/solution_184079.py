def colchao(medidas, H , L):
    '''Função que indica se o colchão passa pela porta.
    lista, int , int -->booleana'''
    if medidas[1] <= H:
        return True
    else:
        return False