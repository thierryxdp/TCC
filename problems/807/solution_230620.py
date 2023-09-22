def conta_frases(x):
    s= (str.count(x,".") + str.count(x,"?") + str.count(x,"...") + str.count(x,"!"))
    if "..." in x:
        s= (str.count(x,"...")) * (-2)
        return s
    else:
        return (str.count(x,".") + str.count(x,"?") + str.count(x,"...") + str.count(x,"!"))