def eh_quadrada(matriz):
    '''uma função que identifica se uma matriz é quadrada.
    matriz -> bool'''
    teste = []
    list.append(teste, len(matriz))
    if teste == []:
        return True
    list.append(teste, len(matriz[0]))
    elif (teste[0] - teste[1] == 0):
        return True
    else:
        return False