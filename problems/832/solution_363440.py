def eh_quadrada(m):
    ''''''
    c=0
    c2=0
    linha = len(m)
    if linha==0:
        return True 
    coluna = len(m[0]) 
    if linha==coluna:
        return True 
    else:
        return False