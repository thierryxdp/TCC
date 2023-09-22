def eh_quadrada(matriz):
    '''funcao que retorna o valor booleano True se a matriz de entrada e quadrada;
    list -> bool'''
    if matriz==[]:
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False