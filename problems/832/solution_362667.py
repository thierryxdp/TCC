def eh_quadrada (matriz=[])
    '''funcao que retorna se uma matriz é quadrada ou nao'''
    '''list[lista] -> bool'''
    if len(matriz)==0:
        return True
    linha = len(matriz)
    coluna = len(matriz[0])
    if linha == coluna:
        return True
    else:
        return False