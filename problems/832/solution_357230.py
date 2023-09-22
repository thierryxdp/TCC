def eh_quadrada(m):
    linha=0
    for i in (len(m)):
        linha=linha+1
        coluna=0
        for j in len(m[0]):
            coluna=coluna+1
    if len(m)==len(m[0]):
        return True
    else:
        return False