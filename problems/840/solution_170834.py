def bolos (a,b,c):
    "calcula a quantidade maxima de bolos possiveis para fazer com os ingredientes dados (int,int,int->int)"
    if a/2==b/3==c/5:
        return int(a/2)
    else:
        return int((a/2)-1)