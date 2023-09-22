def bolos(a,b,c):
    if a/2 > 1 and b <3 and c<5:
        return round((a/2)+0.5)
    if b > 3 and a<2 and c<5:
        return round((b/3)+0.5)
    if c > 5 and a<2 and b<3:
        return round((c/5)+0.5)
    else:
        return 1