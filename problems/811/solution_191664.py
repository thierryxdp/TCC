def colchao(medida, H, L):
    '''dasda'''
    if medida[1]<=H:
        if medida[0]<L and medidas [1]<=H:
            return True
        elif medidas[o]<L and medidas [1]>=H:
        	return False
        elif medida[0]>L and medidas [1]<=H:
            return False
        elif medida[0]>L and medidas [1]>=H:
            return False
	elif medida[1]>H:
        import math
        U=math.sqrt(H**2+L**2)
        t=(U/H)*medidas[0]
        L2=L-t
        if U>medida[1]:
            return True
        else:
            return False