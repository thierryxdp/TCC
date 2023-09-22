def bolos (a,b,c):
    a1=a//2
    b1=b//3
    c1=c//5
    if (a1==b1==c1):
        return a1
    elif (a1 >= b1 >= c1 >= a1):
        return min(a1,b1,c1)
    else:
        return 0