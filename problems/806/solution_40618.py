def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma
     tuple, tuple --> bool'''
    x1a,y1a,x2a,y2a = ret1 
    x1b,y1b,x2b,y2b = ret2 
    if x2b<x1a or x1a<x1b:
        return True
    else:
        xok = False
        return False
    if y2b<y1a or y2a<y1b:
        return True
    else:
        yok = False
        return False
    if xok or yok:
        return False
    else:
        return True