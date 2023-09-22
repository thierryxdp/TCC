from math import ceil
def bolos(A, B, C):
    if A >= 2 and B >= 3 and C >=5:
    	return ceil((A + B + C) / 10)
	else:
        return 0