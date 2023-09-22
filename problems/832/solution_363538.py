def eh_quadrada(matriz):
    '''função que retorna se uma dada matriz é quadrada ou não
    list -> bool'''
    linha = len(matriz)
    if linha == 0:
        return True 
    coluna = len(matriz[0]) 
    if linha == coluna:
        return True 
    else:
        return False