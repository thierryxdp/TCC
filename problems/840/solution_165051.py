import math
def bolos(a,b,c):
    #o número máximo de bolos é limitado pelo ingrediente com menos itens
    a=math.floor(a/2)
    b=math.floor(b/3)
    c=math.floor(c/5)
    return min(a,b,c)