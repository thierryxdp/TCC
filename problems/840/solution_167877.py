"""Retorna a quantidade maxima de bolo que da pra fazer:
int, int, int ->float"""
def bolos(a,b,c):
    if (a<=b and a<=c):
        return float(min(a/2))
    elif (b<=a and b<=c):
        return min(b/3)
    else:
        return min(c/5)