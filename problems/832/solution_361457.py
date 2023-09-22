def eh_quadrada (m):
    ''' '''
    ''' '''
    
    linha = len (m)
    coluna = len(m[0])
    if linha > 0:
        if linha == coluna:
            return True
        else:
            return False
    if linha == 0:
        return True