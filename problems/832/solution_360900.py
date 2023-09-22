def eh_quadrada (m):
    linha= len(m)
    coluna=len(m[0])
    if coluna == 0:
        return True
    if linha==coluna:
        return True
    else:
        return False