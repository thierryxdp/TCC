def eh_quadrada(matriz):
    """ Função que verifica se uma matriz é quadrada ou não 
    list -> bool """
    if matriz==[]:
        return True
    else:
        i=len(matriz)
        j=len(matriz[0])
        if i==j:
            return True
        else:
            return False