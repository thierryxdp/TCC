def eh_quadrada(m, n):
    
    linha = n * [0]
    coluna = m * linha
    
    if len(linha) == len(coluna):
        return True
    else:
        return False