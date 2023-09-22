def colisao (r1,r2):
    xla,yla, x2a,y2a = r1
    xlb,ylb, x2b,y2b = r2
    if x2b < xla or x2a < xlb:
        xok = True
    else:
        xok = False
    if y2b < yla or y2a < ylb:
        yok = True
    else:
        yok= False
    if xok or yok:
        return False
    else: 
        return True