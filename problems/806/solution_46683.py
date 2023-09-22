def colisao(x1, y1, x2, y2, x3, y3, x4, y4):
    if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
        return 'false'
    else:
        return 'true'