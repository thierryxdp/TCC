def eh_quadrada(matriz):
    '''funcao que analisa se a matriz é quadrada. list -> bool'''
    if len(matriz) == 0:
        return True
    for i in range (len(matriz)):
        while i < len(matriz):
            if len(matriz[i]) == len(matriz):
                i += 1
            else:
                 return False
                 return True