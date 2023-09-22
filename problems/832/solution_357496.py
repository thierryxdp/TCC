def eh_quadrada(matriz):
    """ essa função irá identificar se uma matriz é quadrada ou não, sabendo que uma matriz sem linha e nem coluna, tambem será considerada quadrada
    saida -> bool"""
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False