def colisao(ret1,ret2):
    xi1, yi1, xs1, ys1 = ret1
    xi2, yi2, xs2, ys2 = ret2

	if ( xi2 >= xi1 or xi2 <= xs1 ) and ( yi2 >= yi1 or yi2 <= ys1 ):
        col = True
    else:
        col = False
    
    return col