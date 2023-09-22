"""Retorna a quantidade maxima de bolos que Joao consegue fazer:
float, float, float ->int"""
def bolos(a,b,c):
    if (a or b or c)==0:
        return '0'
    else:
        return min((a/2)+(b/3)+(c/5))