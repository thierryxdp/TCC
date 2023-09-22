"""Retorna a quantidade maxima de bolo que da pra fazer:
int, int, int ->int"""
def bolos(a,b,c):
    if (a or b or c)=0:
        return 0
   
    else:
        return min(a,b,c)