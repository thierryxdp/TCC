def colisao(retA,retB):
    x1,y1,X1,Y1=retA 
    x2,y2,X2,Y2=retB 
    if X1<x2:
        return False 
    elif y1>=y2 and Y1<=Y2:
        return True 
    elif X1>=x2 and x1>=X2:
        return True