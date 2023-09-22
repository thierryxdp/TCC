def bolos(a=2,b=3,c=5):
    if a%a == 0 and b%b == 0 and c%c == 0:
        return a/2
    elif a%a != 0 or b%b != 0 or c%c != 0:
        return 0