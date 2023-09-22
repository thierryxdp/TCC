def eh_quadrada(matriz):
    ''' dada uma matriz de entrada ira retornar se ela e quadrada, [list,list] = bool'''
    # so lembrar que len(matriz) = linhas e len(matriz[0]) = coluna
    if len(matriz)==0:
        return True
    elif len(matriz)!=len(matriz[0]):
        return False
    else:
        return True