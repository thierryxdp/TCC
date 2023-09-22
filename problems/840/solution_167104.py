import math
def bolos(A,B,C,min):
    A=math.floor(A/2);
    B=math.floor(B/3);
    C=math.floor(C/5);
    
    min=A;
    if(B<min)
    min=B;
    if(C<min)
    min=C;
    
    return min