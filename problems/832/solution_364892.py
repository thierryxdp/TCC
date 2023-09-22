def eh_quadrada(matriz):
    '''função que recebe uma matriz e verifica se ela é quadrada
    list->bool'''
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if len(matriz)==len(matriz[i]) and len(matriz[j]):
                return True
            else:
                return False