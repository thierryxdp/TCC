def bolos(a, b, c):
    f = a//2
    o = b//3
    l = c//5
    if f==0 or o==0 or l==0:
        return 0
    elif f<o<l:
        return f
    elif f<l<o:
        return f
    elif o<f<l:
        return o
    elif o<l<f:
        return o
    elif l<o<f:
        return l
    elif l<f<o:
        return l