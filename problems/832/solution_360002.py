def eh_quadrada(matriz: list) -> bool:
    """ Indentifica se a matriz dada como parametro de entrada se encaixa
    como uma matriz quadrada.
    ( M(mxn) onde m=n)
    list(list)-> bool """
   	
    if  matriz == [] or (len(matriz) == len(matriz[0])):
        return True
    
    else:
        return False