def conta_frases(x):
    if x.count(".")>0 or x.count("!")>0 or x.count("?")>0:
        k = x.count(".")
    	l = x.count("!")
    	m = x.count("?")
    if x.count("...")>0:
        x.replace("...",".")
        n = x.count(".")
    return k + l + m + n