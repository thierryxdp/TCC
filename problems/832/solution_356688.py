def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada    
    list -> string '''
    if (len(matriz)==len(matriz[0])):
        return True
    else:
        if matriz []:
            return True    
        else:
            return False