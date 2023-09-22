def eh_quadrada (m):
    linha= len(m)
    coluna=len(m[0])
    if linha == 0:
        return True
    if linha==coluna:
        return True
    else:
        return False