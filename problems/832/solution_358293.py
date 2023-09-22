def eh_quadrada(lista):
    '''A função reberá uma lista e a função verificará se a lista é quadrada.
    Dados de entrada -> lista
    Dados de saída -> booleano'''
    
    nlinha = len(lista)
    
    if nlinha == 0:
        return True
    
    ncoluna = len(lista[0])
    
    elif nlinha == ncoluna:
        return True
    
    else:
        return False