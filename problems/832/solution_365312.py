def eh_quadrada(m):
    linha= len(m)
    coluna=len(m[0])
    for i in m:
        if linha == coluna:
            return True
        else:
            return False