def bolos(A,B,C):
    if A%2==0 and B%3==0 and C%5==0:
     return A//2

    if A//2==0 or B//3==0 or C//5==0:
       return 0

    if A%2==1:
       return (A//2)-1 
    if B%3==1 :
       return (B//3)-1
    if C%5==1:
       return (C//5)-1

    else:
       return 0