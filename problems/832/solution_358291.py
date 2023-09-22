def eh_quadrada(lista):
    '''A função reberá uma lista e a função verificará se a lista é quadrada.
    Dados de entrada -> lista
    Dados de saída -> booleano'''
    
    nlinha = len(lista)
    ncoluna = len(lista[0])
    
    if nlinha == 1:
        return True
    
    elif nlinha == ncoluna:
        return True
    
    else:
        return False