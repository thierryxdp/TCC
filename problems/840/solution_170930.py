def bolos(A,B,C):
    if A%2==0 and B%3==0 and C%5==0:
     return A//2
    if A%2==1:
       return A//2 
    if B%3==1:
       return B//3
    if C%5==0:
       return C//5
    else:
     return(A//2)-1