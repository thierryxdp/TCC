def colissao(x1,y1,x2,y2,x3,y3,x4,y4):
    if x2>x3 and x4>x2:
        return True
    elif x3>x2 and x4>x2:
       return False
    elif x3>x2 and x4<x2:
        return True
    elif x4>x1 and x3<x1:
        return True
    elif x4<x1 and x1<x3:
        return True
    elif x4<x1 and x3<x1:
        return False
    elif x1==x4 or x1==x3 or x1==y3 or x1==y4:
        return True
    elif x2==x3 or x2==y3 or x2==x4 or x2==y2:
        return True
    else:
        return False