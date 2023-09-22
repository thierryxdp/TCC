def conta_frases(x):
    if x.count("...")>0:
    	k = x.count("...")
    if x.count("!")>0:
    	k = x.count("!")
    if x.count("?")>0:
    	k = x.count("?")
    if x.count(".")>0:
    	k = x.count(".")
    return k