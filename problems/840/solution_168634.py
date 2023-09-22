def bolos(a=2,b=3,c=5):
    if a < 2 or b < 3 or c < 5:
        return 0*3
    elif a%a == 0 and b%b == 0 and c%c == 0:
        return a/2
    elif a%a == 0 and b%b == 0 and c%c != 0 and c > 5:
        return b/3 
    elif a%a == 0 and b%b != 0 and c%c == 0 and b > 3:
        return c/5
    elif a%a != 0 and b%b == 0 and c%c != 0 and a > 2:
        return b/3
    else:
        return 0*2