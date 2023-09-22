def conta_frases(x):
    s= (str.count(x,".") + str.count(x,"?") + str.count(x,"...") + str.count(x,"!"))
    if "..." in x:
        s= s-3
        return s