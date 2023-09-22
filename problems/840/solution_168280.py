import math
def bolos(A,B,C):
    if min(A,B,C)==A and A>=2 and B>3 and C>5:
        return A/2
    if min(A,B,C)==B and B>=3 and C>5:
        return B/3
    if min(A,B,C)==C and C>=5:
        return C/5
    if (A/2)==1 and (B/3)==1 and (C/5)==1:
        return (A/2+B/3+C/5) 
    else:
        return 0