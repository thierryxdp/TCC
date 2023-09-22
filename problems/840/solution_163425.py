def bolos (a,b,c):
    if a == 0 or b == 0 or c == 0:
        return 0
    else:
        if a < 2 or b < 3 or c < 5:
            return 0
        else:
            return (a+b+c)//10