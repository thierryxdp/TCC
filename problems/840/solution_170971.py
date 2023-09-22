def bolos (A,B,C):
    if (A/2)==(B/3)==(C/5):
        return (A+B+C)/10
    elif (A/2)>(B/3)==(C/5):
        return B
    elif (A/2)==(C/5)<(B/3):
        return A
    elif (A/2)==(B/3)<(C/5):
        return B
    elif (A/2)=!(B/3)=!(C/5):
        return 0