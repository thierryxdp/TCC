def conta_frases(x):
    k = []
    if x.count("...")>0:
    	k =k + x.count("...")
    if x.count("!")>0:
    	k =k + x.count("!")
    if x.count("?")>0:
    	k =k + x.count("?")
    if x.count(".")>0:
    	k =k + x.count(".")
    return k