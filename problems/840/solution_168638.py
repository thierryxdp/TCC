def bolos(a=2,b=3,c=5):
    if a < 2 or b < 3 or c < 5:
        return 0
    elif a%a == 0 and b%b == 0 and c%c == 0:
        return a/2
    elif a%a == 0 and b%b == 0 and c%c != 0 and c > 5:
        if a > b:
            return b//3
        else:
            return a//2
    elif a%a == 0 and b%b != 0 and c%c == 0 and b > 3:
        if a > c:
            return c//5
        else:
            a//2
    elif a%a != 0 and b%b == 0 and c%c == 0 and a > 2:
        if b > c:
            return c//5
        else:
            return b//3
    else:
        return 0