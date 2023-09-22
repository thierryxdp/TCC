"""Retorna a quantidade maxima de bolo que da pra fazer:
int, int, int ->int"""
def bolos(a,b,c):
    if (a<=b and a<=c):
        return (a/2)
    elif (b<=a and b<=c):
        return (b/3)
    elif (c<=a and c<=b):
        return (c/5)
    elif (b>c>a):
        return 0