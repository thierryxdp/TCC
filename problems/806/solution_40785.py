def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com 4 valores int cada.
    tupla->tupla'''
    x1a,y1a,x2a,y2a = ret1
    x1b,y1b,x2b,y2b = ret2
    xok= False
    yok = False
    if x2b < x1a or x1a<x1b:
        return x = True
    else:
        return xok= False
    if y2b<y1a or y2a<y1b:
        return y = True
    else:
        return yok= False
    if xok or yok:
        return False