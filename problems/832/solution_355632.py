def eh_quadrada(matriz):
    ''' Dada uma matriz como entrada, a funcao retorna um booleano que diz se
    eh ou nao quadrada (True para sim e False para nao);
    list -> bool '''
    
    if matriz == []:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False