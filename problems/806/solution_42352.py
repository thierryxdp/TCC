def colisao(tupla1,tupla2):
    
    x1=tupla1[0]
    y1=tupla1[1]
    x2=tupla1[2]
    y2=tupla1[3]

    x3=tupla2[0]
    y3=tupla2[1]
    x4=tupla2[2]
    y4=tupla2[3]

    if x3<=x1 and x1<=x4 and y3<=y1 and y1<=y4:
        return True

    elif x3<=x2 and x2<=x4 and  y3<=y2 and y2<=y4:
        return True
    
    elif x1<=x3 and x3<=x2 and  y1<=y3 and y3<=y2:
        return True

    elif x1<=x4 and x4<=x2 and  y1<=y4 and y4<=y2:
        return True

    else:
        return False