def eh_quadrada(matriz):
    '''Dada uma matriz verifica se ela é ou não quadrada retorando um booleano
    list[list] -> bool'''
    linha = len(matriz)
    coluna = len(matriz[0])
    
    if linha == coluna:
        return True
    elif linha == 0 or matriz == 0:
        return True
    else:
        return False