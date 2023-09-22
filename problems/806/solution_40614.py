def colisao(x1a,y1a,x2a,y2a,x1b,y1b,x2b,y2b):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma
     tuple, tuple --> bool'''
    ret1 = x1a,y1a,x2a,y2a
    ret2 = x1b,y1b,x2b,y2b
    if x2b<x1a or x1a<x1b:
        return True
    else:
        return False
    if y2b<y1a or y2a<y1b:
        return True
    else:
        return False
    if xok or yok:
        return False
    else:
        return True