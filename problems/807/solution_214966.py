def conta_frases(x):
    s = ""
    s = x.replace("...",".")
    if s.count(".")>0 or s.count("!")>0 or s.count("?")>0:
        k = s.count(".")
    	l = s.count("!")
    	m = s.count("?")

    # n = x.count(x.replace("...","."))
    return k + l + m