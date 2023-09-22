#Start your python function here
def colisao(ret1,ret2):
    xla,yla, x2a,y2b = ret1
    xlb,ylb, x2b,y2b = ret2
    if x2b<xla or x2a<xlb:
        xok=True
    else:
        xok=False
    if y2b<yla or y2a<ylb:
        yok=True
    else:
        yok=False
    if xok or yok:
        return False
    else:
        return True