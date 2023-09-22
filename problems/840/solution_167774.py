"""Retorna a quantidade maxima de bolo que da pra fazer:
int, int, int ->int"""
def bolos(a,b,c):
    if (a<=b and a<=c and b>=3 and c>=5):
        return int(a/2)
    elif (b<=a and b<=c and b>=3 and c>=5):
        return int(b/2)
    else:
        return int(c/2)