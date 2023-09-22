def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma
     tuple, tuple --> bool'''
    x1a,y1a,x2a,y2a = ret1 
    x1b,y1b,x2b,y2b = ret2 
    if x1b<x1a or x2a<x2b:
        return True
    else:
        return False
    if y1b<y1a or y2b<y1b:
        return True
    else:
        return False
    if x or y:
        return True
    else:
        return False