def bolos(a, b, c):
    f = a//2
    o = b//3
    l = c//5
    if a==0 or b==0 or c==0:
        print("nao da pra fazer nenhum bolo")
    else if a<b<c:
        return a
    else if b<a<c:
        return b
    else if c<a<b:
        return c