def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com 4 valores int cada.
    tupla->tupla'''
    x1a,y1a,x2a,y2a = ret1
    x1b,y1b,x2b,y2b = ret2
    yok = False
    xok = False
    if x2b<x1a or x2a<x1b:
        x = True
    else:
    if y2b<y1a or y2a<y1b:
        y= True
    if xok or yok:
        return False
    else:
        return True