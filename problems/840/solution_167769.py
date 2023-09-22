"""Retorna a quantidade maxima de bolo que da pra fazer:
int, int, int ->int"""
def bolos(a,b,c):
    if (a<=b and a<=c):
        return (a/2)
    elif (b<=a and b<=c):
        return (b/2)
    else:
        return (c/2)