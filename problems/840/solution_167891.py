"""Retorna a quantidade maxima de bolo que da pra fazer:
float, float, float ->float"""
def bolos(a,b,c):
    if (a<=b and a<=c):
        return min(a/2)
    elif (b<=a and b<=c):
        return min(b/3)
    elif (c<=a and c<=b):
        return min(c/5)
    else:
        return 0