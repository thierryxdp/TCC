def colisao(r1x1,r1y1,r1x2,r1y2,r2x1,r2y1,r2x2,r2y2):
    if r1x1<=r2x1<=r1x2 or r1x1<=r2x2<=r1x2:
        if r1y1<=r2y1<=r1y2 or r1y1<=r2y2<=r1y2:
            return True
    return False