def bolos (A,B,C):
    if (A/2)==(B/3)==(C/5):
        return (A+B+C)/10
    elif (A/2)>(B/3)==(C/5):
        return B
    elif (A/2)==(C/5)<(B/3):
        return A
    elif (A/2)==(B/3)<(C/5):
        return B
    elif (A%2=0)<(B/3)==(C/5):
        return A
    elif (A/2)==(C/5)>(B%3=0):
        return B
    elif (A/2)==(B/3)>(C%5=0):
        return C
    elif (A%2=0)!=(B%3=0)!=(C%5=0):
        return 0