#Start your python function here
def colisao(x1, y1, x2, y2,x3, y3, x4, y4):
    rect1=x1,y1,x2,y2
    rect2=x3,y3,x4,y4
    return rect1 > rect2