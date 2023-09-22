import math
def bolos(A,B,C):
    if min(A,B,C)==A and min(A/2,B/3,C/5)>1:
        return A/2
    elif min(A,B,C)==B and min(A/2,B/3,C/5)>1:
        return B/3
    elif min(A,B,C)==C and min(A/2,B/3,C/5)>1:
        return C/5
    elif 0<(A/2)<1 or 0<(B/3)<1 or 0<(C/5)<1:
        return  0
    elif A/2==1 and B/3==1 and C/5==1:
    	return 1