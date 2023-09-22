import math
def bolos(A,B,C):
    if min(A,B,C)==A and (A/2 and B/3 and C/5)>1:
        return A/2
    if min(A,B,C)==B and (A/2 and B/3 and C/5)>1:
        return B/3
    if min(A,B,C)==C and (A/2 and B/3 and C/5)>1:
        return C/5
    if 0<(A/2)<1 or 0<(B/3)<1 or 0<(C/5)<1:
        return  0
    if A/2==0 or B/3==0 or C/5==0:
    	return 0
    if A/2==1 and B/3==1 and C/5==1:
        return 1