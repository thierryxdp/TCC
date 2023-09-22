def eh_quadrada(lista):
    '''A função reberá uma lista e a função verificará se a lista é quadrada.
    Dados de entrada -> lista
    Dados de saída -> booleano'''
    
    nlinha = len(lista)
    ncoluna = len(lista[0])
    
    if nlinha == ncoluna or nlinha == 0 or ncoluna == 0:
        return True
    else:
        return False