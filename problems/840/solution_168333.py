import math
def bolos(A,B,C):
    if min(A,B,C)==A and A>=2 and B>3 and C>5:
        return A/2
    if min(A,B,C)==B and B>=3 and C>5 and A>2:
        return B/3
    if min(A,B,C)==C and C>=5 and B>3 and A>2:
        return C/5
    if (A/2)<1 or (B/3)<1 or (C/5)<1:
        return  0
	if (A/2)==1 or (B/3)==1 or (C/5)==1: 
    	return A/2
	if 1<(B/3)<(A/2) or 1<(C/5)<(A/2):
    	return (A/2)-1