import math
def bolos (a,b,c):
    '''retorna a quantidade maxima de bolos dados quantidade de ingredientes
    int,int,int->int'''
    return math.floor(min((a/2),(b/3),(c/5)))