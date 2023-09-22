def conta_frases(x):
    k = []
    j = []
    if x.count("...")>0:
    	k =len(k) + j[x.count("...")]
    if x.count("!")>0:
    	k =len(k) + j[x.count("!")]
    if x.count("?")>0:
    	k =len(k) + j[x.count("?")]
    if x.count(".")>0:
    	k =len(k) + j[x.count(".")]
    return k