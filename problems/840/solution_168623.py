def bolos(a=2,b=3,c=5):
    if a%a != 0 or b%b != 0 or c%c != 0:
        return 0
    elif a == 0 or b == 0 or c == 0:
        return 0
    elif a%a == 0 and b%b == 0 and c%c == 0:
        return a/2
    elif a%a == 0 and b&b == 0 and c&c!=0 and c > 5:
        return a/2
    elif a%a == 0 and b&b != 0 and c&c==0 and b > 3:
        return a/2
    elif a%a != 0 and b&b == 0 and c&c==0 and a > 2:
        return b/3
    else:
        return 0