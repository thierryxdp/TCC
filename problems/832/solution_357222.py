def eh_quadrada(m):
    linha=0
    for i in range(m):
        linha=linha+1
        coluna=0
        for j in range(m)[0]:
            coluna=coluna+1
    if linha==coluna:
        return True
    else:
        return False