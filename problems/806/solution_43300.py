def colisao(retA,retB):
    x1,y1,X1,Y1 = retA 
    x2,y2,X2,Y2 = retB 
    if X1>=x2 and (y1,Y1)>=(y2,Y2):
        return True