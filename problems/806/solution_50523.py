def pontos(ret):
    xv1, yx1,xv2, yv2 = ret
    return[(x, y) for x in range(xv1,xv2 + 1) for y in range(yv1, yv2 + 1)]
           
def colisao(ret1, ret2):
	a1 = pontos(ret1)
    a2 = pontos(ret2)
           
    test = False
    for p in a1:
        if (p in a2):
           test = True
           break
    return test