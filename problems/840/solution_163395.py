def bolos(a, b, c):
    f = a//2
    o = b//3
    l = c//5
    if a==0 or b==0 or c==0:
        print("nao da pra fazer nenhum bolo")
    elif a<b<c:
        return a
    elif b<a<c:
        return b
    elif c<a<b:
        return c