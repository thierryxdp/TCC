def inverte(x):
    """..."""
    y= x.replace("."," ")
    z= y.replace("!"," ")
    w= z.replace(","," ")
    g= w.replace("-"," ")
    h= g.replace("?"," ")
    j= str.split(h)
    i= str.join[-1:-(len(j)+1):-1]
    return i