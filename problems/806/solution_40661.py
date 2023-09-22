def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma
     tuple, tuple --> bool'''
    x1a,y1a,x2a,y2a = ret1 
    x1b,y1b,x2b,y2b = ret2 
    if x2a<x1b or x2b<x1a:
        xok = True
    else:
        x = False
    if y2a<y1b or y2b<y1a:
        y = True
    else:
        yok = False
    if xok or yok:
        return False
    else:
        return True