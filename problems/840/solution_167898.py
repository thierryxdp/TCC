"""Retorna a quantidade maxima de bolo que da pra fazer:
int, int, int ->int"""
def bolos(a,b,c):
    if (a<=b and a<=c):
        return (a/2)
    elif (b<=a and b<=c):
        return int(min(b/3))
    elif (c<=a and c<=b):
        return int(min(c/5))
    else:
        return 0