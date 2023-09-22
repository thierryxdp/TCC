def bolos(a=2,b=3,c=5):
    if a%a == 0 and b%b == 0 and c%c==0:
        return a/a
    elif a%a == 0 and b%b == 0 and c%c!=0 and c > 5:
        return a/a
    elif a%a == 0 and b%b != 0 and c%c==0 and b > 3:
        return a/a
    elif a%a != 0 and b%b == 0 and c%c==0 and a > 2:
        return b/b
    elif a%a == 0 and b%b == 0 and c%c!=0 and c < 5:
        return 0
    elif a%a == 0 and b%b != 0 and c%c==0 and b < 3:
        return 0
    elif a%a != 0 and b%b == 0 and c%c==0 and a < 2:
        return 0 
    else:
        return 0