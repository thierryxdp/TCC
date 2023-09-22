#Start your python function here
def colisao(x1, y1, x2, y2, x3, y3, x4, y4):
    colide = x1 <= x3 <= x2 and y1 <= y3 <= y2 or x1<= x4 <= x2 and y1 <= y4 <= y2
    return colide


# segunda etapa - calculo do resultado