def conta_frases(s):
    x= str.split(s,". ",)
    y= str.split(s,"! ",)
    z= str.split(s,"? ",)
    w= str.split(s,"... ",)
    q= str.split(s,".' ",)
	if len(x) == 1:
        x1 = 0
    else:
        x1 = len(x)-1
    if len(y) == 1:
        y1 = 0
    else:
        y1 = len(y)-1
    if len(z) == 1:
        z1 = 0
    else:
        z1 = len(z)-1
    if len(w) == 1:
        w1 = 0
    else:
        w1 = len(w)-1
        x1 -= len(w)-1
    if len(q) == 1:
        x1 += 1
    return x1+y1+z1+w1