def conta_frases(x):
    s= (str.count(x,".") + str.count(x,"?") + str.count(x,"...") + str.count(x,"!"))
    for "..." in x:
        s= s-3
        return s
    else:
        return (str.count(x,".") + str.count(x,"?") + str.count(x,"...") + str.count(x,"!"))