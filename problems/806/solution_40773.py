def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com 4 valores int cada.
    tupla->tupla'''
    x1a,y1a,x2a,y2a = ret1
    x1b,y1b,x2b,y2b = ret2
    if x2b < x1a or x1a<x1b:
        xok = True
    else:
        x = False
    if y2b<y1a or y2a<y1b:
        yok = True
    else:
        y = False
    if x or y:
        return False
    else:
        return True